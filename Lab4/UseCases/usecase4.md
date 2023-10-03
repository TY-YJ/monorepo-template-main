**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: Draw on Canvas using Mouse

**Primary Actor**: User 

**Goal in Context**: 
  - To change pixel colors on the canvas by left-clicking and dragging the mouse
**Preconditions**: 
  - The program is running and ready to accept user input
  - Canvas is displayed

**Trigger**: User left-clicks and holds the mouse button to start drawing.
  
**Scenario**: 
  - The user positions the mouse cursor over the canvas and left-clicks and holds the mouse button to initiate drawing.
  - As the user drags the mouse across the canvas, the system updates the pixel colors to reflect the selected drawing color.
  - It stops drawing when the user unhold left-click.

 
**Exceptions**: 
  - when user use right-click to draw. In this case, ignore input.
  - The program my become potentially unresponsive. In this case, the program can be terminated from the operating system.

**Priority**: High-priority

**When available**: First release

**Channel to Actor**: Mouse input (left-click and drag)

**Secondary Actor**: None

**Channels to Secondary Actors**: N/A

**Open Issues**: We may need to add undo or redo functionallity 

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
