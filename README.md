# Blender 4 Engineers (B4NGN)
		
## Simple and non-invasive add-on for parametric primitives in Blender

This Blender add-on provides easily-accessible shortcuts for parametric geometrical primitives in the already-existing Shift+A menu (exactly where they so obviously belong) No extra buttons, no extra internal-features, no state logic stored in the .blend files themselves. The parametric primitives are implemented using already-existing blender features, and thus completley manually-editable and compatible even when this add-on is absent.

## Features

As of now, three parametric primmitive types are supported:

* Sphere ![]
* Cylinder ![]
* Cuboid ![]

## Installation
	
In order to install, simply download the `B4NGN.py` file to your computer, and use Blender's internal add-on installation utility:
Click `Edit`>`Prefferences`, go to the `Add-ons` tab and click the `Install` button on the top right. This will open Blender's built-in file manager. Simply navigate to the path where you downloaded the file on your computer, select it and press the `Install` button. _It **really** is **that** easy !_

## Usage

The addition parametric geometric primitives is implemented as a set of blender `Operators`. By default, there is no shortcut assigned, so you will have to hit `F3` on your keyboard to bring up a searchbox, in which you should type `Add par...` and the following 3 results will show up:
		* `Add parametric Sphere`
		* `Add parametric Cylinder`
		* `Add parametic Cuboid`
