import { app } from "../../scripts/app.js";

// taken from groupOptions.js by ComfyUI
function addNodesToGroup(group, nodes=[]) {
    var x1, y1, x2, y2;
    var nx1, ny1, nx2, ny2;
    var node;

    x1 = y1 = x2 = y2 = -1;
    nx1 = ny1 = nx2 = ny2 = -1;

    for (var n of [group._nodes, nodes]) {
        for (var i in n) {
            node = n[i]

            nx1 = node.pos[0]
            ny1 = node.pos[1]
            nx2 = node.pos[0] + node.size[0]
            ny2 = node.pos[1] + node.size[1]

            if (node.type != "Reroute") {
                ny1 -= LiteGraph.NODE_TITLE_HEIGHT;
            }

            if (node.flags?.collapsed) {
                ny2 = ny1 + LiteGraph.NODE_TITLE_HEIGHT;

                if (node?._collapsed_width) {
                    nx2 = nx1 + Math.round(node._collapsed_width);
                }
            }

            if (x1 == -1 || nx1 < x1) {
                x1 = nx1;
            }

            if (y1 == -1 || ny1 < y1) {
                y1 = ny1;
            }

            if (x2 == -1 || nx2 > x2) {
                x2 = nx2;
            }

            if (y2 == -1 || ny2 > y2) {
                y2 = ny2;
            }
        }
    }

    var padding = 10;

    y1 = y1 - Math.round(group.font_size * 1.4);

    group.pos = [x1 - padding, y1 - padding];
    group.size = [x2 - x1 + padding * 2, y2 - y1 + padding * 2];
    }


function getContrastColor(hexColor) {
    // Remove the # symbol if it exists
    if (hexColor.startsWith("#")) {
        hexColor = hexColor.slice(1);
    }

    // Expand short hex code to full hex code
    if (hexColor.length === 3) {
        hexColor = hexColor.split('').map(char => char + char).join('');
    }

    // Convert the hex values to decimal (base 10) integers
    const r = parseInt(hexColor.slice(0, 2), 16) / 255;
    const g = parseInt(hexColor.slice(2, 4), 16) / 255;
    const b = parseInt(hexColor.slice(4, 6), 16) / 255;

    // Calculate the relative luminance
    const L = 0.2126 * r + 0.7152 * g + 0.0722 * b;

    // Use the contrast ratio to determine the text color
    return L > 0.210 ? "#000000" : "#999999";
    }


app.registerExtension({
    name: "Aegisflow.NodeTemplate",
    setup(app) {
        setTimeout(() => {
            // Adding a template, creates a group for them
            const originalGetCanvasMenuOptions = LGraphCanvas.prototype.getCanvasMenuOptions;
            LGraphCanvas.prototype.getCanvasMenuOptions = function() {
                const options = originalGetCanvasMenuOptions.apply(this, arguments);
                const nodeTemplatesOption = options.find(option => option && option.content === 'Node Templates');
                if (nodeTemplatesOption && nodeTemplatesOption.submenu && nodeTemplatesOption.submenu.options) {
                    nodeTemplatesOption.submenu.options = nodeTemplatesOption.submenu.options.map(option => {
                        if (option && option.content === 'Manage') {
                            return option;
                        }
                        if (option && typeof option.callback === 'function') {
                            const originalCallback = option.callback;
                            option.callback = function() {
                                originalCallback.apply(this, arguments);
                                const intervalId = setInterval(() => {
                                    if (Object.keys(app.canvas.selected_nodes || {}).length) {
                                        clearInterval(intervalId);
                                        var group = new LiteGraph.LGraphGroup();
                                        group.title = option.content;
                                        addNodesToGroup(group, app.canvas.selected_nodes)
                                        app.canvas.graph.add(group);
                                        app.canvas.graph.change();
                                    }
                                }, 500);
                            };
                        }
                        return option;
                    });
                }
                return options;
            };

            // Changing the color of the node title to be more readable
            const originaldrawNodeShape = LGraphCanvas.prototype.drawNodeShape;
            LGraphCanvas.prototype.drawNodeShape = function() {
                var color = this.current_node.color || "#222";
                this.node_title_color = getContrastColor(color);
                LiteGraph.NODE_TEXT_COLOR = getContrastColor(color);
                originaldrawNodeShape.apply(this, arguments);
            };
        }, 0);
    }
});