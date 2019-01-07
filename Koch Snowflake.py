from turtle import * 

def snowflake(length_side,level):
	if level==0:
		forward(length_side)

	else:
		return 

	length_side=length_side/3.0

	snowflake(length_side,level-1)
	left(60)
	snowflake(length_side,level-1)
	right(120)
	snowflake(length_side,level-1)
	left(60)
	snowflake(length_side,level-1)
	

	if __name__=='__main__':

		speed(0)
		length=300.0

		penup()

		backward(length/2.0)

		pendown()

		for i in range(3):
			snowflake(length,4)
			right(120)

		mainloop()