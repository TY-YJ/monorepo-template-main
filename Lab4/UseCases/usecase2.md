**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 2

<hr>

**Use Case**: Color selection

**Primary Actor**: User

**Goal in Context**: 
  - To allow user to select a drawing color from a predefined set by pressing the correspond number keys (1-8)

**Preconditions**: 
  - The program is running and ready to accept user input
  - Default color is black  
  - Canvas is displayed

**Trigger**: Pressing the number between 1 - 8 to select a color
  
**Scenario**: 
  - A user will press the any number between 1 - 8 to select a desired color.
  - The system validates the input and sets the drawing color to the selected color.
 
**Exceptions**: 
  - When a user presses number beyound 8. In thise case, ignore input.
  - The program my become potentially unresponsive. In this case, the program can be terminated from the operating system.


**Priority**: Medium-priority

**When available**: First release

**Channel to actor**: The user communitcates through keyboard. The system is responsible for maintaining when the user presses number buttons, and should respond within 1 second of the keyboard event. 

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: Colors may be selected by a mouse, so consider adding user experience for selecting a color with a mouse.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
