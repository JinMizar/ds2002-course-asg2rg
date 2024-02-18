#!/bin/bash

clear
echo "Let's build a mad-lib!"

read -p "1. Please give me an adjective: " ADJ1
read -p "2. Please give me a noun: " NOUN1
read -p "3. Please give me a verb: " VERB1
read -p "4. Please give me a adverb: " ADVERB1
read -p "5. Please give me another adjective: " ADJ2
read -p "6. Please give me another noun: " NOUN2
read -p "7. Please give me another verb: " VERB2
read -p "8. Please give me another adverb: " ADVERB2

echo "Once upon a time, in a ${ADJ1} land, there was a ${NOUN1} who loved to ${VERB1} ${ADVERB1}."
echo "Everyone in the kingdom admired its ${ADJ2} beauty, especially the ${NOUN2}."
echo "One day it decided to ${VERB2} ${ADVERB2}, and all who saw it were amazed."
echo "And they all lived happily ever after. The end."
