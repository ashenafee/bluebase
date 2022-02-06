# Bluebase
*Your UTSG course companion.*


![image](https://user-images.githubusercontent.com/20289287/152673250-c78c5222-7970-44b2-bb40-d993d5c29fd6.png)



## Specification

Bluebase is a Discord bot for UofT-St.George campus students to make sure they stay on top of their schedule! Students 
can add the bot to a server and then add, remove and view courses with their lecture, practicals and tutorial timings.
Since this a Discord bot, all of its functionality is available on Discord only.

## Usage

| Command                            | Parameters                                                                                              | Effect                                                       |
|------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| `!help`                            | None                                                                                                    | Shows a help message with all commands.                      |
| `!add <CODE> <SECTION>`            | `CODE`: Course code (i.e. BCH311)<br/> `SECTION`: Course section (i.e. S)                                    | Adds a course to the channel which the message was sent in.  |
| `!remove <CODE>`                   | `CODE`: Course code (i.e. BCH311)                                                                       | Removes a course from the channel the message was sent in.   |
| `!info <CODE> <SECTION>`           | `CODE`: Course code (i.e. BCH311)<br/> `SECTION`: Course section (i.e. S)                                    | Shows information about a course.                            |
| `!view <CODE> <SECTION> <MEETING>` | `CODE`: Course code (i.e. BCH311)<br/> `SECTION`: Course section (i.e. S)<br/> `MEETING`: Meeting type (i.e. LEC) | Shows information about all meetings of a type for a course. |
| `!view_all`                        | None                                                                                                    | Shows information about all the courses in a channel.        |

## What can Bluebase do?

![image](https://user-images.githubusercontent.com/20289287/152673306-88a5b5a6-a451-454c-8800-81d7efe71258.png)


## Scenario walk-through

You're a student with a wide range of courses, although, some relate to each other in one way or another. However, it
becomes really tedious to organize what goes where, and when each thing might happen! Enter, **Bluebase**.

Adding this bot to your Discord server, you're unclear around how it may help and so you ask it precisely that; `!help`

<img width="389" alt="image" src="https://user-images.githubusercontent.com/20289287/152669063-7ee18c9f-d6a6-4add-898d-e74c562cfd2d.png">

To start off, you begin by adding **PCL218**, **IMM250**, and **BCH311** to Bluebase as such:

<img width="593" alt="image" src="https://user-images.githubusercontent.com/20289287/152669101-e62f9201-3887-465a-ab5c-28cda1e04957.png">

Curious, you want to see if your additions really persisted, and so you call `!view_all`:

<img width="467" alt="image" src="https://user-images.githubusercontent.com/20289287/152669135-8cfd0faa-8754-4cc6-b702-bb4ed1d9bd74.png">

Content with your courses being added, your curious nature again gets the best of you. This time, however, it's to get a bit of a primer
on what awaits you in **BCH311**:

<img width="595" alt="image" src="https://user-images.githubusercontent.com/20289287/152669183-bcb4ed78-94f7-4b45-bd13-fd68059ab907.png">

Woah! That's a lot of content. It's a good thing the exclusions are listed there because I'm sure you were tempted to pursue **MGY311**
as well as **BCH311**! Enough about BCH though. You're curious about when your cannabis lectures are:

<img width="388" alt="image" src="https://user-images.githubusercontent.com/20289287/152669243-f84aeb8f-9a66-470c-8a22-a232a67d5953.png">

Let's hope you've got the time on Mondays/Wednesdays!

## How does our project relate to "Restoration"?

Having lived lives straight out of dystopian novels for the past 2 years, we are sure that the thought of "normal" has crossed everyone's
minds - especially the minds of students. Having to learn handfuls of content through a screen and a pair of headphones is an entirely new
world, one we learned to traverse as the days went by.

In recent times, we are seeing things go back to normal - a restoration of life if you will. Slowly but surely, people are able to partake
in their regular pre-pandemic activities, parties can be held, and students can get back to the hustle and bustle of campus life.

With this restoration comes the relevance of a timetable skyrocketing once more. [Discord](https://www.discord.com) has become an integral
part of many students' lives throughout pandemic learning, especially from what we, Team Base, have noticed in several UofT servers.

By bringing the functionality and usefulness of a course browser to an interface we've come to know and love, we at Team Base set out with
the goal of restoring the idea of what once was normal, but we came across a revelation along the way... Why not combine the two worlds we've
grown so used to? Through restoring the sense of normalcy, and preserving the ease of online, we have the birth of **Bluebase - A bot that helps
you organize your UofT courses**.

## What's next for Bluebase?

![image](https://user-images.githubusercontent.com/20289287/152673285-b182d032-829a-470c-832e-5291f1e28c91.png)

