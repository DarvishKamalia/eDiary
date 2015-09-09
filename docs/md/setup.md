Setup
=====
before the workshop
-------------------

In order to teach coding, it makes life simpler if every student is on the same
operating system. Why? Because Windows 7 does things in one way, Windows 8 does
things in another way, OS X does things in a third way, etc. Hence, we will all
use a common operating system, and that operating system is called Ubuntu.
We're choosing to use Ubuntu because it is the most popular (and the best
suited) OS for coding. 

You will not have to install Ubuntu on your laptops. Instead, you will have to
install a small piece of software called VirtualBox. VirtualBox is a tool which
allows you to run another OS inside your current OS. This another OS is
called the *guest* OS and your current OS is called the *host* OS. Hence, in
our case, the *host* OS of every student will be different (Windows, Mac, etc),
but the *guest* OS of every student will be the same (Ubuntu). And we will work
exclusively in the *guest* OS. 

### Steps to install VirtualBox (henceforth referred to as VBox):

- If you're on **Windows**, download VBox from [here][win]
- If you're on a **Mac**, download VBox from [here][mac]
- Install it like you would install any other application

### Steps to get Ubuntu as guest OS inside VBox:

- Open VBox, go to **File**, inside that go to **Import Appliance...**
- In the dialog box that opens up, browse through the files in your computer
  and choose the `Ubuntu.ova` file we gave you yesterday (via pen drives)
- Click **Next**, and then click **Import** (without changing any options)
- Wait patiently until the import process finishes (it should take around 5
  minutes)
- Once it's done, you should see a new OS called 'Ubuntu' in the left-pane of
  VBox
- That's it, you can now run it by right-clicking on it and choosing **Start**
- The username and password to be used on this guest Ubuntu OS are both `icode`

If you're successfully able to do all of this before the intervention, nothing
like it. If you run into some issues (many of you will, simply because you're
all on different computers with different operating systems), don't worry,
we'll help you get set up during the intervention. :)

### Known issues

For some of you, it is possible that you get an error after
clicking on **Import** in the above steps (i.e. the error happens in the middle
of the import process). If this is happening to you, you need to use a
different `.ova` file, namely `Ubuntu_32.ova` (instead of the original
`Ubuntu.ova`). This is also a roughly 2 GB file, so we're sending two pen
drives containing this file to school with Aaryaa tomorrow morning. Just take the
file from her and do the above steps again to get set up. :)

[win]: http://download.virtualbox.org/virtualbox/5.0.0/VirtualBox-5.0.0-101573-Win.exe
[mac]: http://download.virtualbox.org/virtualbox/5.0.0/VirtualBox-5.0.0-101573-OSX.dmg