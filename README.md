# LED Dim Switch

This MicroPython script was written for a Raspberry Pi Pico, allowing you to control the level of brightness of an individual LED using a potentiometer. It goes beyond the raw input and converts the input to an exponential value, giving a much smoother control over the brightness of the LED. Without that exponential value, the LED doesn't fully turn off with a low potentiometer value, and the transition of brightness is jumpy. You also don't notice much difference in the brightness of the higher values. With the exponent, you can see the full range of brightness and control precisely how bright you want the LED to be.

# Background

Similar to my [simulation of an LED heat sensor](https://github.com/tenshi-net/potentiometer-heat-sensor), this script is based off of a lesson in Paul McWhorter's excellent [Raspberry Pi Pico course series](https://www.youtube.com/playlist?list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5). I originally started learning Python as a side skill to aid in my pursuit of being a penetration tester, but with a recent change in career direction toward embedded/IoT security, I've been turning my microcontroller/SBC hobby into part of my career. Since doing so, Python and coding concepts as a whole have made much more sense to me, perhaps because I see the physical results of what I write.

I don't claim any ownership of this because, as I said, it's based off of Paul's code in lesson 11. I did make some slight modifications to the layout, variable names, and I also tweaked the print output so each value is on its own line with a descriptor, hopefully to aid in debugging.

Speaking of debugging, I hope other people can use this as a basis to develop portions of their projects. Feel free to merge the code into your existing projects. I aim to use this as a foundation for anything I need a potentiometer-based dimmable LED for.

# How it works

The script's logic is simple. It checks the current value of the potentiometer and then assigns it to its own variable (`pot_val`). From there, it gets an exponential value (`exp_val`) of the potentiometer value in bits. There's an independent brightness variable (`bright_val`) that is 2 to the power of whatever the exponential value is currently assigned as. From there, the red LED variable 16-bit duty cycle value is assigned as whatever the brightness variable is.

In other words, the LED is controlled by the brightness variable. That variable, in turn, is a result of getting an exponent of the current value of the potentiometer and raising 2 to the power of the exponent variable. The exponent variable is meant to convert the raw bits to the exponential value.

I'm not great at math, so I may be misunderstanding some of what's actually happening, but that's the way I understand it.

# Important

As with my "heat sensor" project, make sure you set the `pot_pin` and `led_pin` variables to match the appropriate pins you have hooked up on your breadboard. If you want an approximation of how I laid things out on my own breadboard, check the corresponding [Wokwi sketch](https://wokwi.com/projects/468423416633181185).
