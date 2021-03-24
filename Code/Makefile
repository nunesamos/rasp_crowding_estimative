rce: main.o take5pic.o
	gcc $(CFLAGS) -o rce main.o take5pic.o
main.o: ./src/main.c ./include/take5pic.h
	gcc $(CFLAGS) -c ./src/main.c 
take5pic.o: ./src/take5pic.c ./include/take5pic.h
	gcc $(CFLAGS) -c ./src/take5pic.c
clean:
	rm -f *.o rce