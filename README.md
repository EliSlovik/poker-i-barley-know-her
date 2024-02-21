# poker-i-barely-know-her 
https://replit.com/@9730820/poker-barley-thing#main.py

## Group members and roles:
* Eli Slovik: Project manager and designer
* Aidan Slovik: Coder and designer
* Adam Kolb: Researcher and tester

A chair, a ladder, and a phone are playing poker, the ladder says, "I raise", the phone thinks for a second, then says, "I call", then, the chair thinks for a while, and disgruntily says, "I fold"

Group Leader: Create a GitHub repository for the project with a clever name and add group members as collaborators 
Write each known class for project (class name, constructor, member variables and known methods without logic)
Write and test the main class play screen including all items from the GUI mockup i.e. score panel, grid layout, map or whatever is going to be rendered in the running of the app outside of start screen and end screen
Create a class diagram to include all variables and methods

### Classes and methods:
* main
  * constructor method
  * deal card
* calc hand strength
  * Royal flush check
  * Straight flush check
  * four of a kind check
  * flush check
  * straigh check
  * three of a kind check
  * two pair check
  * pair chech




##Class Diagram   
*HAND ---------> CARDS________>DEALER HAND
                  *|               |             |      \\
                  *|               |             | 
                  *|                |             |
                 * CARD number     VALUES        DEALER VALUE
                   *|                 |               |                       
                    *|                 |               |
                    *ALL CARDS       VALUE TOTAL      DEALER TOTAL VALUE
                                      * |                | 
                                       * |                |
                                        *|                |
                                       * --------|---------
                                               *  |
                                                * |
                                                 *|
                                                 *WINNER ------------>PAYOUT
