<<<<<<< HEAD
rce: main.o takepic.o
	gcc $(CFLAGS) -o rce main.o takepic.o
main.o: ./src/main.c ./include/takepic.h
	gcc $(CFLAGS) -c ./src/main.c 
takepic.o: ./src/takepic.c ./include/takepic.h
	gcc $(CFLAGS) -c ./src/takepic.c
=======
rce: main.o take5pic.o
	gcc $(CFLAGS) -o rce main.o take5pic.o
main.o: ./src/main.c ./include/take5pic.h
	gcc $(CFLAGS) -c ./src/main.c 
take5pic.o: ./src/take5pic.c ./include/take5pic.h
	gcc $(CFLAGS) -c ./src/take5pic.c
>>>>>>> 07fbd9d7cfc9bb16c976d2e78c1f25dcb22ae50d
clean:
	rm -f *.o rce ./pics/*