# aegisflow_utility_nodes
The Utility nodes have a variety of "Passer" nodes that can both passs through items targeted by Use Everywhere nodes, as well as secure an input that requires one. This is necessary because Comfy will try to "fix" those inputs using any output that matches, even if that doesn't work, breaking the wf (this is an "all workflows problem, not an AegisFlow problem.

Most commonly used is an "image" passer, but you can do others like latents,masks, CLIP etc. There is also a "Placeholder Tuple" for times when you need to fill a Tuple but aren't going to actually use it. This is helpful in developing template workflows that are frequently broken when inputs are left unoccupied (ask me how I know?)

![image](https://github.com/aegis72/aegisflow_utility_nodes/assets/118572301/f1157839-d454-4622-b5cd-b39a26678fec)


There is also the "multipasser" which gangs them all together so they can be collapsed into the "superlaser."

![image](https://github.com/aegis72/aegisflow_utility_nodes/assets/118572301/21eeb471-9247-4463-aca8-5437e1f6640a)


##Ally's Nodes, with an extension
I was having many users unable to satisfy some great nodes from the ally and thusly integrated them here, and extended them with an "enable/disable" switch. 

##Auto Grouping of Nodes placed as templates
Thanks to mortael, we now have nodes that group automaticallywhen placed in a template, and name themselves after the template name. This is a key QOL improvement that also ensures we can take full advantage of Chris Goringe's Use Everywhere nodes using AegisFlow Shima, which recently added in execution control via group name.

![autogrouping](https://github.com/aegis72/aegisflow_utility_nodes/assets/118572301/4147c1c1-2170-474c-b750-55545184ed9b)


##Auto Contrast node text contrast
Do you hate the color palette limitations of ComfyUI? I DO. I hate that "yellow" is considered that "burnt ochre" color that you threw away from your crayons because it's so gross. Problem is, until now that was all it could be: the color of the text is greay and the text of the coloring shall be grey. It meant that without developing an entirely new theme, you couldn't use high-brightness colors at all.

![image](https://github.com/aegis72/aegisflow_utility_nodes/assets/118572301/caea02a0-1872-4356-bccd-efa6efdd7594)


The world was a dark place. It was a dark time. But now, color can come back into your WFs:

![image](https://github.com/aegis72/aegisflow_utility_nodes/assets/118572301/23d4439c-1848-4976-8137-d8e727cdb5ce)
