##
## EPITECH PROJECT, 2021
## B-CNA-410-LIL-4-1-groundhog-alexis.roye
## File description:
## Makefile
##

all	:	
		cp groundhog.py groundhog
		chmod +x groundhog

clean:
	rm groundhog

fclean: clean

re: fclean all