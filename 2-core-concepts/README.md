# Core Concepts

This module gives a brief overview of the core concepts / components in a Choregraphe project. The intention of this module is to give the reader a high-level understanding of how a Choregraphe project flows. Daniel Schofield does a great job explaining much of the fundamental concepts of Choregraphe and Pepper on his YouTube channel. I would recommend watching his videos first before continuing with this documentation.

## Reference

Official documentation:

- [Main objects](http://doc.aldebaran.com/2-5/software/choregraphe/main_objects.html)

Watch [this 2-part YouTube video playlist by Daniel Schofield](https://www.youtube.com/watch?v=tqVbX5NWFdU&list=PLmXbV-2dNm43SH6HG88LALwFPs2TQIGpa). The vidoes go over QiChat (used in Dialog boxes) and Python scripts in Choregraphe boxes.

# Boxes

The smallest and most basic unit / component in a Choregraphe project is the box. Each box on the canvas consists of a set of inputs, a set of outputs, and the logic within the box that connects the two. This logic can be Python code, a Dialog script, or more boxes!

To create a box:

- If a developer wants to use a built-in box... Find the box in the box library panel and then drag and drop the box onto the canvas.
- If a developer wants to create a custom box... Right click, hover over "Create a new box", and then choose between Python, Dialog, or Diagram depending on what kind of logic is required.

<img src="img/ui-right-click.png" />

Python boxes are controlled by Python code. Although Choregraphe's built-in boxes provides logic boxes (loops, if-clauses, etc.), it is recommended to try and put all logic within a Python box instead. By using the built-in boxes, the canvas can get cluttered and become difficult to understand; too many boxes on the canvas. If the developer expects complex logic or a functionality not provided by a built-in Choregraphe box, use a Python box.

Dialog boxes should be used when the developer expects a conversation between Pepper and a user. At a high-level, QiChat script allows defining a set of text to listen for with the corresponding reply. If the developer expects a dialogue or conversation, use the dialog box.

When a project begins to get big, the developer may need to start looking at creating diagram boxes. These boxes allow defining the logic using other boxes (nested box logic). Below is the internal logic for the "Record Sound" box.

<img src="img/ui-nested-box.png" />

When there is a need to break up the code into smaller, more manageable components or when designing with reusability in mind, then the developer should consider using diagram boxes.

NOTE: Timeline boxes are used with animations and animation mode, which is covered in a later module.

# Connectors

Boxes are the smallest and most basic unit / component. When they interact with each other, their capabilities expand. To create connectors between one box's output to another box's input, simply click and drag from the output to the input.

The entrypoint for the program is on the left of the canvas while the stopping point is at the right. It is good practice to always provide at least one route from the entrypoint to the stopping point.
