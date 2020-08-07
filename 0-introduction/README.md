# Introduction

Pepper is a social robot (made by Aldebaran, later bought by Softbank) used in commerce for various service-related tasks: as receptionists, store attendants, etc. Automating tedious and oftentimes repetitive tasks are a hallmark for robots; however, social robots are an opportunity to automate a broader range of tasks. Much of the research on human-robot interfaces and interactions focus on how humans respond to robots in place of a human actor. Which tasks are viable for robot automation? To what extent should these tasks be automated by robots? Is the definition of "automation" different when talking about social robots? Even with these questions, social robots have already found real-life applications: geriatric care and therapy for children with autism in healthcare. Social robots as autonomous actors in our daily lives are the reason why I find social robots interesting. For my CIS 4900 Independent Study (Summer 2020) project, I wanted to learn how to program Pepper using Choregraphe.

Thank you, Dr. John Licato and the Advancing Machine and Human Reasoning (AMHR) research lab, for letting me use Pepper over the summer semester.

[![AMHR Logo](img/amhr-logo.png)](https://sites.google.com/view/amhr/home?authuser=0)

## What is Choregraphe?

From the [official documentation](http://doc.aldebaran.com/2-5/software/choregraphe/choregraphe_overview.html):

> Choregraphe is a multi-platform desktop application, allowing you to:
>
> - Create animations, behaviors and dialogs,
> - Test them on a simulated robot, or directly on a real one,
> - Monitor and control you robot,
> - Enrich Choregraphe behaviors with your own Python code.
>
> Choregraphe allows you to create applications containing Dialogs, services and powerful behaviors, such as interaction with people, dance, e-mails sending, without writing a single line of code.

It is a desktop application used to create robot applications for NAO robots. It features a nice drag-and-drop flowchart interface that makes programming more graphical rather than textual.

## Why use Choregraphe?

Choregraphe provides a way to program Pepper using a drag-and-drop flowchart graphical interface. This is similar to [MIT's Scratch programming language for children](https://scratch.mit.edu/). An intuitive interface allows a greater range of people from different disciplines to also work with Pepper. So why spend an entire summer learning Choregraphe's "intuitive" interface? Although the concept is intuitive, the documentation is obscure and lacking.

## Goal

With sparse documentation from Aldebaran and Softbank, the goal for this independent study project is to generate documentation (this GitHub repository) detailing how to accomplish the following:

- [x] Retrieve readings from all of Pepper's sensors
- [x] Send commands to all of Pepper's actuators
- [ ] Get images and videos from Pepper's camera(s)
- [x] Get sound and text from Pepper's microphone(s)
- [x] Output sound and speech
- [x] Displaying images, videos, etc. on Pepper's tablet

Moreover, the final module will be a small project showing how to integrate [Google Cloud Speech-To-Text API](https://cloud.google.com/speech-to-text), [Django](https://www.djangoproject.com/), and Pepper together to collect and store text transcribed from audio.

## Scope

While Softbank provides developers various software and toolkits to program their robots, this independent study project will only look at how to program using Choregraphe and Python. The following modules will assume that the reader understands [how to take care of Pepper](http://doc.aldebaran.com/2-5/home_pepper.html) and [basic Python syntax](https://www.python.org/doc/).

## Further Project Ideas

The following ideas are beyond the scope of this independent study project, but may be promising and interesting projects.

> Choregraphe is not the only way to program Pepper. Softbank has [SDKs](http://doc.aldebaran.com/2-5/dev/programming_index.html) in several programming languages: C++, Python, and JavaScript to name a few. Programming using these SDKs may be a natural next step after learning how to use Choregraphe to program Pepper.

> What seems to be new documentation for QiSDK emerged this year 2020. What's promising is that, not only is it up to date, but it moves away from Aldebaran documentation and towards Softbank documentation (Aldebaran developed Pepper and NAO before the company's acquisition by Softbank). Developing using QiSDK on the Android Studio IDE may be a promising project in the future. Relevant references:  [Softbank Robotics Developer Center](https://developer.softbankrobotics.com/pepper-qisdk) and [QiSDK](https://qisdk.softbankrobotics.com/sdk/doc/pepper-sdk/index.html).

## Author

My name is Marc Gabriel N. Badilla. At the time of writing this, I am a fourth-year computer science student at the University of South Florida (USF).

[<img src="img/linkedin-logo.png" width="10%" height="10%" />](https://www.linkedin.com/in/marcbad/)
