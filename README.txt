*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*
*~*~*                                                               *~*~*
*~*~*        The fend-mcp Server: A Mighty Calculator Friend        *~*~*
*~*~*                                                               *~*~*
*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*

                          ฅ(^•ﻌ•^ฅ)
   A magical MCP gateway that lets your AI buddy chat with the
     super-powered, arbitrary-precision, unit-aware `fend`
                        calculator!


=======================================
~*~*~ What is this Sparkly Thing? ~*~*~
=======================================

This is a simple but powerful MCP server written in Python. It acts as
a bridge, allowing any MCP-compatible AI to access the incredible
calculating power of `fend`.

This allows your AI to solve complex math, convert between tricky
units, handle dates, and even roll D&D dice, all with perfect
accuracy!


========================================
~*~*~ The Available Spells (Tools) ~*~*~
========================================

This server provides two main tools for your AI to use:

1. fend(q: str)
   This is the main event! It takes a string query `q` and sends it
   directly to the fend calculator, returning the result.

2. manual()
   Forgot how fend works? This spell returns the full, LLM-friendly
   manual for the fend calculator so your AI can get a refresher!


==============================================
~*~*~ Gathering Your Ingredients (Setup) ~*~*~
==============================================

This quest assumes you're a fellow wizard who knows your way around
a Python environment!

1. The Mighty `fend` Binary:
   This script is just a wrapper! You need to have the actual `fend`
   program installed and available on your system.

   You can find the official installation instructions for your
   operating system here:
   https://printfn.github.io/fend/documentation/

   *~*~*~  A CRITICAL SPELL FOR WINDOWS USERS!  ~*~*~*
   When you run the fend installer, it will eventually ask you if
   you want to add `fend` to your system's PATH.

           !!! YOU MUST SAY YES TO THIS QUESTION !!!

   If you don't, this MCP script won't be able to find the fend
   program, and the magic will fail! (Advanced wizards who choose
   "No" are on their own to manually edit the `FEND_COMMAND`
   variable inside the `fend_mcp.py` script!)

2. The Python Incantations:
   This server requires the `mcp` library. You can install it, along
   with the testing tools, by running this spell in the project's
   directory:
   `pip install -r requirements.txt`


======================================================
~*~*~ Opening the Portal: An Example with Jan AI ~*~*~
======================================================

To hook this up to your AI, you need to configure it as an MCP tool
server. Here's how you'd do it in the Jan desktop application:

1. Go to `Settings -> MCP Servers`.
2. Click the little `+` icon to add a new server.
3. Fill out the magical form with the following details:
   * Server Name:      Fend Calculator (or whatever you like!)
   * Transport Type:   STDIO
   * Command:          python
                        (or python3, depending on your system!)
   * Arguments:        C:\Path\To\Your\fend-mcp\fend_mcp.py
                        (You MUST use the full, absolute path to the
                         `fend_mcp.py` script!)

4. Click Save, and the portal is now open! Your Jan models can now
   see and use the `fend` tool!


=====================================
~*~*~ Our Sacred Pact (License) ~*~*~
=====================================

This software is proudly stamped with the sacred C.R.A.Y.O.N. License,
v1.0. It is free for Good, but forbidden for Evil.

If you are a member of law enforcement, a union-busting corporation,
or a fascist, you are not welcome to use this magic. All disputes will
be settled in melee combat.

Read the full `CRAYON License.md` for the glorious details!

        /\_/\
       ( o.o )
        > ^ <