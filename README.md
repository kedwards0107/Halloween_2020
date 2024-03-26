![](giphy.gif)


<p>
 For the second iteration of the Halloween project we wanted to add dispensing which was definitely a challenge because each candy was a different size and shape. Additionally, I wanted to minimize the number of motors needed to dispense the candies. In the end, I decided to go with a rack and pinion design which only used two motors. Due to covid, we also decided to use motion sensors to activate the dispensing so that the trick-or-treaters wouldn't need to press a button, they would simply place their bag under the ramp to activate the dispensing. Well... that was the idea anyway.
  
  Very similar in terms of components to the 2019 build, we used a raspberry pi 3 and a breadboard to connect a 4 terminal relay switch, 4 led fairy string lights for the "arrows", 2 stepper motors and 4 motion sensors.

In addition, I designed and 3D printed mounts for the motors as well as the rack and pinions. Python was used as the programming language. When you placed your bag/hand under the ramp for a given candy it activated the motor in the direction needed to dispense the candy, additionally it activated a switch attached to that particular candy's led lights which would flash on and off 6 times, and also updated a google sheets chart which was shown on an ipad in the cabinet. We also printed a QR code so that, if people were interested in which candy won at the end of the night, they could take a picture of it and it would send them to the google sheet.

As the build was only for one night we continued to use the quick connects and breadboard in the design. It is great to be able to re-use the components for other projects or for next year's Halloween project. Unfortunately, the cabinet design had to change, but as you can see many of the wood parts are made from scraps of other projects. The big cost was definitely the plexiglass which was much more expensive in 2020 due to covid.

We learned quickly Halloween night that there were several issues with this design. For one, the movement of the rack and pinion had to be precise to dispense the candy and return to the original starting position. Unfortunately, there were several times it got stuck or misaligned which required manually resetting it. Additionally, as day faded into night the light sensors did not activate properly or activated completely on their own. It was definitely a learning experience!
</p>
