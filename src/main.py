# Random pixel fader 2017-09-25 Zafar Iqbal < ultrasine@gmail.com >

from sense_hat import SenseHat

import time 
import random 

sense = SenseHat( )
sense.clear( )
sense.low_light = True

list1 = [
     [ 0 , 0 ] , [ 1 , 0 ] , [ 2 , 0 ] , [ 3 , 0 ] , [ 4 , 0 ] , [ 5 , 0 ] , [ 6 , 0 ] , [ 7 , 0 ] ,
     [ 0 , 1 ] , [ 1 , 1 ] , [ 2 , 1 ] , [ 3 , 1 ] , [ 4 , 1 ] , [ 5 , 1 ] , [ 6 , 1 ] , [ 7 , 1 ] ,
     [ 0 , 2 ] , [ 1 , 2 ] , [ 2 , 2 ] , [ 3 , 2 ] , [ 4 , 2 ] , [ 5 , 2 ] , [ 6 , 2 ] , [ 7 , 2 ] ,
     [ 0 , 3 ] , [ 1 , 3 ] , [ 2 , 3 ] , [ 3 , 3 ] , [ 4 , 3 ] , [ 5 , 3 ] , [ 6 , 3 ] , [ 7 , 3 ] ,
     [ 0 , 4 ] , [ 1 , 4 ] , [ 2 , 4 ] , [ 3 , 4 ] , [ 4 , 4 ] , [ 5 , 4 ] , [ 6 , 4 ] , [ 7 , 4 ] ,
     [ 0 , 5 ] , [ 1 , 5 ] , [ 2 , 5 ] , [ 3 , 5 ] , [ 4 , 5 ] , [ 5 , 5 ] , [ 6 , 5 ] , [ 7 , 5 ] ,
     [ 0 , 6 ] , [ 1 , 6 ] , [ 2 , 6 ] , [ 3 , 6 ] , [ 4 , 6 ] , [ 5 , 6 ] , [ 6 , 6 ] , [ 7 , 6 ] ,
     [ 0 , 7 ] , [ 1 , 7 ] , [ 2 , 7 ] , [ 3 , 7 ] , [ 4 , 7 ] , [ 5 , 7 ] , [ 6 , 7 ] , [ 7 , 7 ]
]

while True :

    random.shuffle( list1 )

    c = [ random.randint( 0 , 255 ) , random.randint( 0 , 255 ) , random.randint( 0 , 255 ) ]

    for i in range( len( list1 ) ) :

        sense.set_pixel( list1[ i ][ 0 ] , list1[ i ][ 1 ] , c )

        time.sleep( 60.0 / 64.0 )    

