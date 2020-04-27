import API
import os
import click

@cli.command()
def Main():
  click.echo("Command line initialized, enter -h for help:")

@cli.command()
def rootTest():
  root()

@cli.command()
@click.option("--Factorial", prompt="The number you want to factor:", help="The number you want factored.")  
def factorialTest(Factorial):
  Fact1(Factorial)
  
@cli.command() 
@click.option("--Fibonacci", prompt="How many numbers you want Fibonacci'd", help="The amount of places to see in the Fibonacci Sequence.")
def fibonacciTest(Fibonacci):
  fibo(Fibonacci)
  
@cli.command()  
@click.option("--Prime", prompt="The number to test", help="The number we want to check if is prime.")
def primeTest(Prime):
  prime(Prime)
  
@cli.command()  
@click.option("--Slack", prompt="Your message", help="The message to post on slack.")
def SlackMessage(Slack):
  send_message_to_slack(Slack)
  
@cli.command() 
@click.option("--keyRecord", prompt="Your desired key to input", help="The key to add.")
def keyRecorder(keyRecord):
  record(keyRecord)
  
@cli.command()  
@click.option("--keyRetrieve", prompt="Your desired key to retrieve", help="The key to find.")
def keyRetriever(keyRetrieve):
  retrieve(keyRetrieve)

if __name__ == '__main__':
  cli()
