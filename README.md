# DevOps Technical Challenges

Thank you for reviewing my challenge, I have left some additional comments and thoughts on the test as I went through them.

## Comments about challenges

1. The concept of this challenge was simple and I have broken down the steps into functions. There is a bit of repeated code to fetch the stats for each pokemon and it is important to note that it would be hard to maintain adding more variables like pokemon3, pokemon 4 etc. If this script was to be improved to handle any amount of arguments I would store these in a key value structure like a dictionary and use loops to iterate over all the arguments

2. I am most comfortable on Ubunti/Debian based linux images so I choose Ubuntu as the base and used version 20.04 as that is the LTS release. Containers have been given names in the docker-compose file as specificed by the challenge but an important note is this restricts the ability to scale multipe containers https://docs.docker.com/compose/compose-file/compose-file-v3/#container_name

3. I have only used ansible occasionally, mainly for a similar task of copying over a bashrc config file to remote servers but I believe all tasks have been successfully completed
