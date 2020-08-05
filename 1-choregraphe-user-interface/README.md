# Choregraphe User Interface

This module gives a brief overview of the Choregraphe user interface. This will introduce an initial set of panels that will be useful when developing using Choregraphe. The panels discussed here are by no means the only panels; other panels will be discussed when it is used in later modules. Daniel Schofield does a great job explaining much of the fundamental concepts of Choregraphe and Pepper on his YouTube channel. I would recommend watching his videos first before continuing with this documentation.

The image below is an example of what a Choregraphe project may look like (this is the Choregraphe project from the final module).

![UI Overview Example](img/ui-overview.PNG)

## Reference

Official documentation:

- [Menus, Panels and Toolbar in a glance](http://doc.aldebaran.com/2-5/software/choregraphe/interface.html)
- [Main Panels](http://doc.aldebaran.com/2-5/software/choregraphe/starting_discovery.html)
- [Advanced Panels](http://doc.aldebaran.com/2-5/software/choregraphe/advanced_panels.html)

Watch [this 5-part YouTube video playlist by Daniel Schofield](https://www.youtube.com/watch?v=wSoGO1iL_v4&list=PLmXbV-2dNm40-19AfOc_0Ie_3hR-7nwMo). The vidoes go over the Choregraphe UI as well as foundational concepts for programming using Choregraphe.

# User Interface

## Header

![Header](img/ui-header-menu.PNG)

The header provides easy access to common tasks and functions:

- `File`: manage Choregraphe project files
- `Connection`: manage [remote connections (via LAN or Ethernet)](http://doc.aldebaran.com/2-4/software/choregraphe/connection_widget.html) to your robots
- `View`: display certain panels in the user interface; if you do not see the panel being discussed, check that the panel is being shown here

Below these menu sets are the most common tasks and functions (provided as a convenience). These functions should be self-explanatory; hovering over each button will give you a tooltip.

## Canvas

![Canvas Panel](img/ui-canvas.PNG)

The canvas panel will be where all your project's logic will be found, so be prepared to spend much of your time in this panel. In the previous module, Choregraphe provides a flowchart interface. A Choregraphe project's flow of control moves from left to right, activating a box's functions when its corresponding control lines are triggered. More will be said about the logic in the next module.

## Project Files

![Project Files Panel](img/ui-project-files.PNG)

The project files panel will be where the developer can view all files for the Choregraphe project. The `behavior_1/behavior.xar` file represents the project's canvas. At the bottom, you can switch between `Project files` and `Project objects`; project files was already discussed, so project objects lists all boxes in the entire project (disregarding the current canvas being displayed).

## Box Library

![Box Library Panel](img/ui-box-library.PNG)

The box library panel displays all boxes available to Choregraphe. The libraries displayed above are all built-in Choregraphe libraries. Here, you can import your own library (out of scope for this independent study project).

## The Right-Hand Side

![Right-Hand Side Panels](img/ui-right-panels.PNG)

The right-hand side of the interface consists of the robot view and inspector panels.

On the robot view panel, `Robot view` displays a 3D model of the NAO robot while `Video monitor` streams what the NAO robot is currently seeing.

When you have a box selected, you can view its properties in the inspector panel.
