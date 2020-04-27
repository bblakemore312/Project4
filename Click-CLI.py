import API
import os
import click

@click.option("--Factorial", prompt="The number you want to factor:", help="The number you want factored.")
@click.option("--Fibonacci", prompt="How many numbers you want Fibonacci'd", help="The amount of places to see in the Fibonacci Sequence.")
@click.option("--Prime", prompt="The number to test", help="The number we want to check if is prime.")
@click.option("--Slack", prompt="Your message", help="The message to post on slack.")
@click.option("--keyRecord", prompt="Your desired key to input", help="The key to add.")
@click.option("--keyRetrieve", prompt="Your desired key to retrieve", help="The key to find.")

