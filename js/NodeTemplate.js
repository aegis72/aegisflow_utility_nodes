import { app } from "../../scripts/app.js";

// Define a custom node that selects an image based on a property (imageIndex), maintains aspect ratio
class aflogo extends LiteGraph.LGraphNode {
    constructor() {
        super();
        this.title = "AegisFlow Logo";

        this.isVirtualNode = true;

        // Add a property for the image index and RGBA color overlay
        this.addProperty("imageIndex", 0, "number", { min: 0, max: 25, title: "Image Index" });
        this.addProperty("version", "20240302", "string", { title: "version" });
        this.image = null; // To store the loaded image
        this.imageAspectRatio = 1; // Default aspect ratio
        this.loadImageByIndex(this.properties.imageIndex); // Load initial image based on index

        // Set the initial title of the node to include the version
        this.title = "\u00A0" + this.properties.version;
        this.bgcolor = "rgba(31,31,31,0)";
        this.color = "rgba(31,31,31,0)";
        this.title = "\u00A0";

        // Optional: Add a dummy input and output to satisfy application requirements
        //    this.addInput("input", null);  // The type can be adjusted based on your needs
        //    this.addOutput("output", null); // The type can be adjusted based on your needs
    }
    // Method to load the image based on the provided index
    loadImageByIndex(index) {
        // Ensure the index is within bounds
        var url = aflogo.imageURLs[Math.max(0, Math.min(index, aflogo.imageURLs.length - 1))];
        this.loadImage(url);
    }
    // Method to load the image from URL
    loadImage(url) {
        var img = new Image();
        img.src = url;
        img.onload = () => {
            this.image = img;
            this.imageAspectRatio = img.width / img.height;
            this.setDirtyCanvas(true, true); // Redraw the node
        };
    }
    // Override the onPropertyChanged method to react to property changes
    onPropertyChanged(name, value) {
        if (name == "imageIndex") {
            this.loadImageByIndex(value);
            this.setDirtyCanvas(true, true); // Redraw the node
        }

        if (name === "version") {
            // Update the node's title to reflect the new version
            this.title = "v." + value;
            this.setDirtyCanvas(true, true); // Redraw the node
        }
        this.setDirtyCanvas(true, true); // Redraw the node to reflect the title change
        return true; // Indicate the property change has been handled
    }
    // Override onDrawBackground to display the image with aspect ratio preservation and apply an RGBA color overlay
    onDrawBackground(ctx) {
        if (!this.image) return; // Don't draw anything if the node is collapsed or the image isn't loaded


        // Aspect ratio preservation code...
        var nodeWidth = this.size[0];
        var nodeHeight = this.size[1];
        var nodeAspectRatio = nodeWidth / nodeHeight;
        var drawWidth, drawHeight;

        // Calculate the size of the image to be drawn based on the node's aspect ratio
        if (this.imageAspectRatio > nodeAspectRatio) {
            drawWidth = nodeWidth;
            drawHeight = drawWidth / this.imageAspectRatio;
        } else {
            drawHeight = nodeHeight;
            drawWidth = drawHeight * this.imageAspectRatio;
        }

        var x = (nodeWidth - drawWidth) / 2;
        var y = (nodeHeight - drawHeight) / 2;

        ctx.drawImage(this.image, x, y, drawWidth, drawHeight);
    }
}

function randomString(length) {
    return Math.round((Math.pow(36, length + 1) - Math.random() * Math.pow(36, length))).toString(36).slice(1);
}

// List of hardcoded image URLs
aflogo.imageURLs = [
    "https://www.majorstud.io/wp-content/uploads/2024/02/shimasquareonly.png", // 0 Default and "else" image
    "https://www.majorstud.io/wp-content/uploads/2024/02/1a_15_loader.png", //1
    "https://www.majorstud.io/wp-content/uploads/2024/02/1b_15_sampler.png",//2
    "https://www.majorstud.io/wp-content/uploads/2024/02/2a_xl_loader.png",//3
    "https://www.majorstud.io/wp-content/uploads/2024/02/2b_xl_sampler.png",//4
    "https://www.majorstud.io/wp-content/uploads/2024/02/3a_Ctrlstack.png",//5
    "https://www.majorstud.io/wp-content/uploads/2024/02/3b_ctrlinput.png",//6
    "https://www.majorstud.io/wp-content/uploads/2024/02/3c_ctrlproc.png",//7
    "https://www.majorstud.io/wp-content/uploads/2024/02/4a_img2img.png",//8
    "https://www.majorstud.io/wp-content/uploads/2024/02/5a_ipmix.png",//9
    "https://www.majorstud.io/wp-content/uploads/2024/02/6a_fxpipe.png",//10
    "https://www.majorstud.io/wp-content/uploads/2024/02/6b_maskfx.png",//11
    "https://www.majorstud.io/wp-content/uploads/2024/02/7a_iterate.png",//12
    "https://www.majorstud.io/wp-content/uploads/2024/02/8a_uu.png",//13
    "https://www.majorstud.io/wp-content/uploads/2024/02/9a_faces.png",//14
    "https://www.majorstud.io/wp-content/uploads/2024/02/10_saver.png",//15
    "https://www.majorstud.io/wp-content/uploads/2024/02/11_segsu.png",//16
    "https://www.majorstud.io/wp-content/uploads/2024/02/shima-alltext.png",//17
    "https://www.majorstud.io/wp-content/uploads/2024/02/shima-square-logo-text.png",//18
    "https://www.majorstud.io/wp-content/uploads/2024/02/shima-wide.png",//19
    "https://www.majorstud.io/wp-content/uploads/2024/02/shimasquareonly.png",//20
    "https://www.majorstud.io/wp-content/uploads/2024/02/ms-badge.png",//21
    "https://www.majorstud.io/wp-content/uploads/2024/02/ms-logo-wide.png",//22
    "https://www.majorstud.io/wp-content/uploads/2024/02/comparator.png",//23
    "https://www.majorstud.io/wp-content/uploads/2024/02/supersaver.png",//24
    "https://www.majorstud.io/wp-content/uploads/2024/03/ctrl-paint.png",//25    
];


// Register the node in LiteGraph
LiteGraph.registerNodeType("AegisFlow/aflogo", aflogo);


// taken from groupOptions.js by ComfyUI
export function addNodesToGroup(group, nodes=[]) {
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
                                        group.title = option.content + "_" + randomString(3);
                                        group.color = "#454545";
                                        addNodesToGroup(group, app.canvas.selected_nodes)
                                        app.canvas.graph.add(group);
                                        app.canvas.graph.change();
                                        LGraphCanvas.active_canvas.deselectAllNodes();
                                    }
                                }, 500);
                            };
                        }
                        return option;
                    });
                }
                return options;
            };

            const originalGetGroupMenuOptions = LGraphCanvas.prototype.getGroupMenuOptions;
            LGraphCanvas.prototype.getGroupMenuOptions = function(node) {
                const options = originalGetGroupMenuOptions.apply(this, arguments);
                const group = this.graph.getGroupOnPos(this.graph_mouse[0], this.graph_mouse[1]);
                if (group) {
                    group.recomputeInsideNodes();
                    const nodesInGroup = group._nodes;
                    options.push({
                        content: `Remove group with nodes`,
                        callback: () => {
                            LGraphCanvas.onMenuNodeRemove('', '', '', '', node); // maybe very hacky, but it works :)
                            nodesInGroup.forEach(node => {
                                LGraphCanvas.onMenuNodeRemove('', '', '', '', node);
                            });
                        }
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
                LiteGraph.NODE_SELECTED_TITLE_COLOR = getContrastColor(color);
                originaldrawNodeShape.apply(this, arguments);
            };
        }, 0);
    }
});
