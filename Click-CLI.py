import API
import os
import click

@click.command()
@click.option("--Factorial", prompt="The number you want to factor:", help="The number you want factored.")
@click.option("--Fibonacci", prompt="How many numbers you want Fibonacci'd", help="The amount of places to see in the Fibonacci Sequence.")
@click.option("--Prime", prompt="The number to test", help="The number we want to check if is prime.")
@click.option("--Slack", prompt="Your message", help="The message to post on slack.")
@click.option("--keyRecord", prompt="Your desired key to input", help="The key to add.")
@click.option("--keyRetrieve", prompt="Your desired key to retrieve", help="The key to find.")

def rootTest(funcTest):
  root()

def factorialTest(Factorial):
  Fact1(Factorial)
  
def fibonacciTest(Fibonacci):
  fibo_send(Fibonacci)
  
def primeTest(Prime):
  prime(Prime)
  
def SlackMessage(Slack):
  send_message_to_slack(Slack)
  
def keyRecorder(keyRecord):
  record(keyRecord)
  
def keyRetriever(keyRetrieve):
  retrieve(keyRetrieve)


