#!/bin/python
######################################################################
#(C)2017 Zafar Iqbal <ultrasine@gmail.com>
### imports
from __future__ import division
import time
import signal
import os
import sys
import json
import pygame
import random 
import copy
import commands
import math
import pprint
import collections
imports_clock_ = int( time.time( ) * 1000 )
imports_clockt_ = -1
def imports_Loopskip_( t ) :
    global imports_clock_
    imports_clockt_ = clock_Difference( imports_clock_ )
    if( imports_clockt_ < t ) : return( True )
    imports_clock_ = imports_clock_ + imports_clockt_
    return( False )
def imports_Log_( ln , m = "" ) :
    log_Write( "imports_:" + str( ln ) , m )
def imports_Config_( k , v = None ) :
    return( config_Query( "imports_" , k , v ) )
def imports_ConfigLocal_( k , v = None ) :
    return( config_Query( "imports_" , "imports_" + k , v ) )
def imports_Action_( a ) :
    gamemaster_Action( "imports_" , a )
imports_enabled = False
def imports_Enabled_( v = None ) :
    global imports_enabled
    cfg = imports_Config_( "imports_" )
    if(cfg==None): 
        if( v == None ) :
            return( imports_enabled )
        imports_enabled = v
        return
    if(cfg=="y"):
        return( True )
    return( False )
def imports_Exit_( ) :
    imports_Log_( "43:47:imports_Log_( \"EXIT\" )" , "EXIT" )
    _PROGSHUTDOWN_( )
### util
def util_JSONload( path ) :
    if os.path.isfile( path ) :
        with open( path ) as f :
            try:
                data = json.load( f )
            except:
                f.close( )
                util_Log_( "8:57:util_Log_( path + \" Bad Json?\")" , path + " Bad Json?")
                util_Exit_( )
            f.close( )
    else:
        util_Log_( "12:61:util_Log_( path + \" not found\" )" , path + " not found" )
        return( { } )
    data = util_Convert( data )
    return( data )
def util_JSONsave( path , data ) :
    try:
        with open( path , "w" ) as f :
                json.dump( data , f )    
                f.close( )
    except:
        util_Log_( "22:71:util_Log_( \"JSON Save \" + path )" , "JSON Save " + path )
        util_Exit_( )
def util_Convert( data ) :
    if isinstance( data , basestring ) :
        return str( data.encode( "utf-8" ) )
    elif isinstance( data , collections.Mapping ) :
        return dict( map( util_Convert , data.iteritems( ) ) )
    elif isinstance( data, collections.Iterable ) :
        return type( data )( map( util_Convert , data ) )
    else:
        return data
util_clock_ = int( time.time( ) * 1000 )
util_clockt_ = -1
def util_Loopskip_( t ) :
    global util_clock_
    util_clockt_ = clock_Difference( util_clock_ )
    if( util_clockt_ < t ) : return( True )
    util_clock_ = util_clock_ + util_clockt_
    return( False )
def util_Log_( ln , m = "" ) :
    log_Write( "util_:" + str( ln ) , m )
def util_Config_( k , v = None ) :
    return( config_Query( "util_" , k , v ) )
def util_ConfigLocal_( k , v = None ) :
    return( config_Query( "util_" , "util_" + k , v ) )
def util_Action_( a ) :
    gamemaster_Action( "util_" , a )
util_enabled = False
def util_Enabled_( v = None ) :
    global util_enabled
    cfg = util_Config_( "util_" )
    if(cfg==None): 
        if( v == None ) :
            return( util_enabled )
        util_enabled = v
        return
    if(cfg=="y"):
        return( True )
    return( False )
def util_Exit_( ) :
    util_Log_( "62:111:util_Log_( \"EXIT\" )" , "EXIT" )
    _PROGSHUTDOWN_( )
### log
log_filehandle = None
log_buildid = "*"
log_runs = "*"
log_pp = pprint.PrettyPrinter( )
# DO NOT CALL LOG WRITE IN THIS METHOD
def log_( ) :
    global log_filehandle
    if not os.path.isdir( "cache" ) :
        os.mkdir( "cache" )
    log_filehandle = open( "cache/default.log" , "a" , 0 )
def log_Setup( ) :
    global log_buildid , log_runs
    log_buildid = log_Config_( "buildid" )
    log_runs = log_Config_( "runs" )
    if( log_runs == None ) :
        log_runs = "!"
    else :
        log_runs = str( log_runs )
    if( log_buildid == None ) :
        log_buildid = "!"
    else:
        log_buildid = str( log_buildid )
def log_Shutdown( ) :
    global log_filehandle
    if( log_filehandle != None ) :
        log_filehandle.write( "\n" )
        log_filehandle.close( )
        log_filehandle = None
def log_Write( x , msg = "" ) :
    global log_filehandle , log_buildid , log_runs
    if( log_filehandle != None ) :
        t = time.strftime( "%Y%m%d%H%M%S" )
        s = "\n" + log_buildid + ":" + log_runs + ":" + t + " , " + x + " , " + str( msg ) + "\n" ;
        #s = log_pp.pformat(msg)
        try:
            log_filehandle.write( s ) 
        except:
            print( "log_ WRITE PASS??? [" + msg + "]" )
log_clock_ = int( time.time( ) * 1000 )
log_clockt_ = -1
def log_Loopskip_( t ) :
    global log_clock_
    log_clockt_ = clock_Difference( log_clock_ )
    if( log_clockt_ < t ) : return( True )
    log_clock_ = log_clock_ + log_clockt_
    return( False )
def log_Log_( ln , m = "" ) :
    log_Write( "log_:" + str( ln ) , m )
def log_Config_( k , v = None ) :
    return( config_Query( "log_" , k , v ) )
def log_ConfigLocal_( k , v = None ) :
    return( config_Query( "log_" , "log_" + k , v ) )
def log_Action_( a ) :
    gamemaster_Action( "log_" , a )
log_enabled = False
def log_Enabled_( v = None ) :
    global log_enabled
    cfg = log_Config_( "log_" )
    if(cfg==None): 
        if( v == None ) :
            return( log_enabled )
        log_enabled = v
        return
    if(cfg=="y"):
        return( True )
    return( False )
def log_Exit_( ) :
    log_Log_( "68:181:log_Log_( \"EXIT\" )" , "EXIT" )
    _PROGSHUTDOWN_( )
### config
config_internal = None
config_external = None
config_custom = None
def config_( ) :
    global config_internal , config_external , config_custom
    config_external = util_JSONload( "cache/config.json"  )
    config_internal = {"box":"b1","release":"1","buildid":132,"parent":"mp","time":1506440158,"extconfigpath":"cache\/config.json"} # Keep newline! 
    config_custom = util_JSONload( "cache/.custom.json" )
    if( "runs" in config_custom ) :
        config_custom[ "runs" ] = config_custom[ "runs" ] + 1
    else:
        config_custom[ "runs" ] = 1
        #config_custom[ "orientation" ] = "0"
    util_JSONsave( "cache/.custom.json" , config_custom )
def config_Query( m , k , v = None ) :
    global config_internal , config_external , config_custom
    if v == None :
        if k in config_external :
            return( config_external[ k ] )
        elif k in config_internal :
            return( config_internal[ k ] )
        elif k in config_custom :
            return( config_custom[ k ] )
        else:
            #Not reccommended due to ENABLED MACRO
            #config_Log_( "26:209:#config_Log_( \"NO CONFIG \" + m + \",\" + k )" , "NO CONFIG " + m + "," + k )
            return( None )
    config_custom[ k ] = v
    util_JSONsave( "cache/.custom.json" , config_custom )
config_clock_ = int( time.time( ) * 1000 )
config_clockt_ = -1
def config_Loopskip_( t ) :
    global config_clock_
    config_clockt_ = clock_Difference( config_clock_ )
    if( config_clockt_ < t ) : return( True )
    config_clock_ = config_clock_ + config_clockt_
    return( False )
def config_Log_( ln , m = "" ) :
    log_Write( "config_:" + str( ln ) , m )
def config_Config_( k , v = None ) :
    return( config_Query( "config_" , k , v ) )
def config_ConfigLocal_( k , v = None ) :
    return( config_Query( "config_" , "config_" + k , v ) )
def config_Action_( a ) :
    gamemaster_Action( "config_" , a )
config_enabled = False
def config_Enabled_( v = None ) :
    global config_enabled
    cfg = config_Config_( "config_" )
    if(cfg==None): 
        if( v == None ) :
            return( config_enabled )
        config_enabled = v
        return
    if(cfg=="y"):
        return( True )
    return( False )
def config_Exit_( ) :
    config_Log_( "59:242:config_Log_( \"EXIT\" )" , "EXIT" )
    _PROGSHUTDOWN_( )
### signal
def signal_Handler( signal , frame ) :
    signal_Exit_( )
signal.signal( signal.SIGTERM , signal_Handler )
signal.signal( signal.SIGINT , signal_Handler )
signal_clock_ = int( time.time( ) * 1000 )
signal_clockt_ = -1
def signal_Loopskip_( t ) :
    global signal_clock_
    signal_clockt_ = clock_Difference( signal_clock_ )
    if( signal_clockt_ < t ) : return( True )
    signal_clock_ = signal_clock_ + signal_clockt_
    return( False )
def signal_Log_( ln , m = "" ) :
    log_Write( "signal_:" + str( ln ) , m )
def signal_Config_( k , v = None ) :
    return( config_Query( "signal_" , k , v ) )
def signal_ConfigLocal_( k , v = None ) :
    return( config_Query( "signal_" , "signal_" + k , v ) )
def signal_Action_( a ) :
    gamemaster_Action( "signal_" , a )
signal_enabled = False
def signal_Enabled_( v = None ) :
    global signal_enabled
    cfg = signal_Config_( "signal_" )
    if(cfg==None): 
        if( v == None ) :
            return( signal_enabled )
        signal_enabled = v
        return
    if(cfg=="y"):
        return( True )
    return( False )
def signal_Exit_( ) :
    signal_Log_( "34:278:signal_Log_( \"EXIT\" )" , "EXIT" )
    _PROGSHUTDOWN_( )
### clock
def clock_( ) :
    clock_Update( )
    pass
def clock_Loop( ) :
    time.sleep( 0.01 )
    clock_Update( )
    pass
def clock_Update( ) :
    global clock_clock_
    clock_clock_ = int( time.time( ) * 1000 )
    pass
def clock_Get( ) :
    global clock_clock_
    return( clock_clock_ )
def clock_Difference( c ) :
    return( clock_Get( ) - c )
clock_clock_ = int( time.time( ) * 1000 )
clock_clockt_ = -1
def clock_Loopskip_( t ) :
    global clock_clock_
    clock_clockt_ = clock_Difference( clock_clock_ )
    if( clock_clockt_ < t ) : return( True )
    clock_clock_ = clock_clock_ + clock_clockt_
    return( False )
def clock_Log_( ln , m = "" ) :
    log_Write( "clock_:" + str( ln ) , m )
def clock_Config_( k , v = None ) :
    return( config_Query( "clock_" , k , v ) )
def clock_ConfigLocal_( k , v = None ) :
    return( config_Query( "clock_" , "clock_" + k , v ) )
def clock_Action_( a ) :
    gamemaster_Action( "clock_" , a )
clock_enabled = False
def clock_Enabled_( v = None ) :
    global clock_enabled
    cfg = clock_Config_( "clock_" )
    if(cfg==None): 
        if( v == None ) :
            return( clock_enabled )
        clock_enabled = v
        return
    if(cfg=="y"):
        return( True )
    return( False )
def clock_Exit_( ) :
    clock_Log_( "46:326:clock_Log_( \"EXIT\" )" , "EXIT" )
    _PROGSHUTDOWN_( )
### timer
timer_timer = None
timer_action = None
timer_clock = None
def timer_( )  :
    timer_Enabled_( False )
def timer_Setup( )  :
    global timer_timer
    timer_timer = 0
def timer_Loop( ) :
    if not timer_Enabled_( ) : return
    if timer_Loopskip_( 1 ) : return
    global timer_timer
    global timer_action
    global timer_clock
    delta = timer_timer -  ( int( time.time( ) * 1000 ) - timer_clock )
    #timer_Log_( "16:344:#timer_Log_(delta)" ,delta)
    if( delta < 0 ) :
        #timer_Log_( "18:346:#timer_Log_( \"Trigger Action \" + timer_action )" , "Trigger Action " + timer_action )
        # Always disable before running action!
        timer_Enabled_( False )
        timer_Action_( timer_action )
def timer_Set( action = "NOP" , t = 0 ) :
    global timer_timer
    global timer_action
    global timer_clock
    timer_timer = t
    timer_action = action
    timer_clock = int( time.time( ) * 1000 )
    timer_Enabled_( True )
    #timer_Log_( "30:358:#timer_Log_( \"SET \"+str(timer_timer)+\" \"+action)" , "SET "+str(timer_timer)+" "+action)
timer_clock_ = int( time.time( ) * 1000 )
timer_clockt_ = -1
def timer_Loopskip_( t ) :
    global timer_clock_
    timer_clockt_ = clock_Difference( timer_clock_ )
    if( timer_clockt_ < t ) : return( True )
    timer_clock_ = timer_clock_ + timer_clockt_
    return( False )
def timer_Log_( ln , m = "" ) :
    log_Write( "timer_:" + str( ln ) , m )
def timer_Config_( k , v = None ) :
    return( config_Query( "timer_" , k , v ) )
def timer_ConfigLocal_( k , v = None ) :
    return( config_Query( "timer_" , "timer_" + k , v ) )
def timer_Action_( a ) :
    gamemaster_Action( "timer_" , a )
timer_enabled = False
def timer_Enabled_( v = None ) :
    global timer_enabled
    cfg = timer_Config_( "timer_" )
    if(cfg==None): 
        if( v == None ) :
            return( timer_enabled )
        timer_enabled = v
        return
    if(cfg=="y"):
        return( True )
    return( False )
def timer_Exit_( ) :
    timer_Log_( "60:388:timer_Log_( \"EXIT\" )" , "EXIT" )
    _PROGSHUTDOWN_( )
### watchdog
def watchdog_Loop( ) :
    #if watchdog_Loopskip_( 1000 ) : return
    if watchdog_Loopskip_( 900000 ) : return
    watchdog_Log_( "4:394:watchdog_Log_( \"woof\" )" , "woof" )
watchdog_clock_ = int( time.time( ) * 1000 )
watchdog_clockt_ = -1
def watchdog_Loopskip_( t ) :
    global watchdog_clock_
    watchdog_clockt_ = clock_Difference( watchdog_clock_ )
    if( watchdog_clockt_ < t ) : return( True )
    watchdog_clock_ = watchdog_clock_ + watchdog_clockt_
    return( False )
def watchdog_Log_( ln , m = "" ) :
    log_Write( "watchdog_:" + str( ln ) , m )
def watchdog_Config_( k , v = None ) :
    return( config_Query( "watchdog_" , k , v ) )
def watchdog_ConfigLocal_( k , v = None ) :
    return( config_Query( "watchdog_" , "watchdog_" + k , v ) )
def watchdog_Action_( a ) :
    gamemaster_Action( "watchdog_" , a )
watchdog_enabled = False
def watchdog_Enabled_( v = None ) :
    global watchdog_enabled
    cfg = watchdog_Config_( "watchdog_" )
    if(cfg==None): 
        if( v == None ) :
            return( watchdog_enabled )
        watchdog_enabled = v
        return
    if(cfg=="y"):
        return( True )
    return( False )
def watchdog_Exit_( ) :
    watchdog_Log_( "34:424:watchdog_Log_( \"EXIT\" )" , "EXIT" )
    _PROGSHUTDOWN_( )
### events
#events_ev = pygame.event.Event( pygame.USEREVENT , e = "entity1" , a = "attr1" , v = "val1") 
#    pygame.event.post ( ev )
def events_Setup( ) :
    pygame.init( )
    #pygame.display.set_mode( ( 640 , 480 ) )
    #pygame.event.set_blocked( pygame.MOUSEMOTION )a
def events_Shutdown( ) :
    pygame.quit( )    
def events_Loop( ) :
    if events_Loopskip_( 10 ) : return
    pygame.event.pump( )
    for event in pygame.event.get( ) :
        #events_Log_( "13:439:#events_Log_( event.type )" , event.type )
        if event.type == pygame.QUIT :
            events_Exit_( )
        elif event.type == pygame.KEYDOWN :
            #events_Log_( "17:443:#events_Log_( event.mod )" , event.mod )
            #events_Log_( "18:444:#events_Log_( event.key )" , event.key )
            if event.key == pygame.K_SPACE :
                events_Action_( "BUTTONDOWN" )
                pass
            elif event.key == pygame.K_ESCAPE :
                events_Exit_( )
            elif event.key == pygame.K_o :
                events_Action_( "ORIENTATION" )
            else:
                pass
events_clock_ = int( time.time( ) * 1000 )
events_clockt_ = -1
def events_Loopskip_( t ) :
    global events_clock_
    events_clockt_ = clock_Difference( events_clock_ )
    if( events_clockt_ < t ) : return( True )
    events_clock_ = events_clock_ + events_clockt_
    return( False )
def events_Log_( ln , m = "" ) :
    log_Write( "events_:" + str( ln ) , m )
def events_Config_( k , v = None ) :
    return( config_Query( "events_" , k , v ) )
def events_ConfigLocal_( k , v = None ) :
    return( config_Query( "events_" , "events_" + k , v ) )
def events_Action_( a ) :
    gamemaster_Action( "events_" , a )
events_enabled = False
def events_Enabled_( v = None ) :
    global events_enabled
    cfg = events_Config_( "events_" )
    if(cfg==None): 
        if( v == None ) :
            return( events_enabled )
        events_enabled = v
        return
    if(cfg=="y"):
        return( True )
    return( False )
def events_Exit_( ) :
    events_Log_( "57:483:events_Log_( \"EXIT\" )" , "EXIT" )
    _PROGSHUTDOWN_( )
### state
state_previous = None 
state_current = None 
state_changed = None
def state_( ) :
    global state_state
    global state_current
    global state_changed
    state_previous = "UNKNOWN" 
    state_current = "BOOT" 
    state_changed = True
def state_Query( v = None ) :
    global state_previous
    global state_current
    global state_changed
    if v == None :
        return( state_current )
    state_previous = state_current 
    state_current = v
    state_changed = True
    state_Log_( "20:505:state_Log_( state_previous + \" -> \" + state_current )" , state_previous + " -> " + state_current )
    return( v )
def state_Unchanged(  ) :
    global state_changed
    if( state_changed ) :
        state_changed = False
        return( False )
    return( True ) 
state_clock_ = int( time.time( ) * 1000 )
state_clockt_ = -1
def state_Loopskip_( t ) :
    global state_clock_
    state_clockt_ = clock_Difference( state_clock_ )
    if( state_clockt_ < t ) : return( True )
    state_clock_ = state_clock_ + state_clockt_
    return( False )
def state_Log_( ln , m = "" ) :
    log_Write( "state_:" + str( ln ) , m )
def state_Config_( k , v = None ) :
    return( config_Query( "state_" , k , v ) )
def state_ConfigLocal_( k , v = None ) :
    return( config_Query( "state_" , "state_" + k , v ) )
def state_Action_( a ) :
    gamemaster_Action( "state_" , a )
state_enabled = False
def state_Enabled_( v = None ) :
    global state_enabled
    cfg = state_Config_( "state_" )
    if(cfg==None): 
        if( v == None ) :
            return( state_enabled )
        state_enabled = v
        return
    if(cfg=="y"):
        return( True )
    return( False )
def state_Exit_( ) :
    state_Log_( "57:542:state_Log_( \"EXIT\" )" , "EXIT" )
    _PROGSHUTDOWN_( )
### sensehat
sensehat_data = { }
sensehat_data[ "available" ] = False
try :
    from sense_hat import SenseHat
    sensehat_data[ "available" ] = True
except :
    pass
def sensehat_( ) :
    pass
def sensehat_Setup( ) :
    if sensehat_Query( "available" ) :
        sensehat_Query( "sense" , SenseHat( ) ) 
        sensehat_Query( "sense" ).clear( )
        sensehat_Query( "sense" ).low_light = True
        #sensehat_Query( "sense" ).set_imu_config( False , True , False )  
        sensehat_Query( "width" , 8 )
        sensehat_Query( "height" , 8 )
        sensehat_Query( "dirty" , True )
        sensehat_Query( "fb" , [
                             [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] ,
                             [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] ,
                             [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] ,
                             [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] ,
                             [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] ,
                             [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] ,
                             [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] ,
                             [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ]
                        ] )
def sensehat_Query( k , v = None ) :
    global sensehat_data
    if v == None :
        return( sensehat_data[ k ] )
    sensehat_data[ k ] = v
def sensehat_Loop( ) :
    if sensehat_Loopskip_( 100 ) : return
    if not sensehat_Query( "available" ) : return
    for event in sensehat_Query( "sense" ).stick.get_events( ) :
        if event.action == "pressed" and event.direction == "middle" :
            sensehat_Action_( "BOOT" )
    sensehat_Query( "pitch" , sensehat_Query( "sense" ).get_orientation( )[ "pitch" ] )
    sensehat_Query( "roll" , sensehat_Query( "sense" ).get_orientation( )[ "roll" ] )
    sensehat_Query( "yaw" , sensehat_Query( "sense" ).get_orientation( )[ "yaw" ] )
    if not sensehat_Query( "dirty" ) : return
    #fb = copy.deepcopy( sensehat_Query( "fb" ) )
    #fb[random.randint(0,63)]=[100,100,0]
    sensehat_Query( "sense" ).set_pixels( sensehat_Query( "fb" ) )
    sensehat_Query( "dirty" , False )
sensehat_clock_ = int( time.time( ) * 1000 )
sensehat_clockt_ = -1
def sensehat_Loopskip_( t ) :
    global sensehat_clock_
    sensehat_clockt_ = clock_Difference( sensehat_clock_ )
    if( sensehat_clockt_ < t ) : return( True )
    sensehat_clock_ = sensehat_clock_ + sensehat_clockt_
    return( False )
def sensehat_Log_( ln , m = "" ) :
    log_Write( "sensehat_:" + str( ln ) , m )
def sensehat_Config_( k , v = None ) :
    return( config_Query( "sensehat_" , k , v ) )
def sensehat_ConfigLocal_( k , v = None ) :
    return( config_Query( "sensehat_" , "sensehat_" + k , v ) )
def sensehat_Action_( a ) :
    gamemaster_Action( "sensehat_" , a )
sensehat_enabled = False
def sensehat_Enabled_( v = None ) :
    global sensehat_enabled
    cfg = sensehat_Config_( "sensehat_" )
    if(cfg==None): 
        if( v == None ) :
            return( sensehat_enabled )
        sensehat_enabled = v
        return
    if(cfg=="y"):
        return( True )
    return( False )
def sensehat_Exit_( ) :
    sensehat_Log_( "77:621:sensehat_Log_( \"EXIT\" )" , "EXIT" )
    _PROGSHUTDOWN_( )
### gamemaster
def gamemaster_( ) :
    pass
def gamemaster_Setup( ) :
    wizard_CheckSecurity( )
def gamemaster_Loop( ) :
    if( state_Unchanged( ) ) :
        return
    state = state_Query( )
    if( state == "BOOT" ) :
        timer_Set( "ATTRACT" )
        pass
    elif( state == "ATTRACT" ) :
        timer_Set( "IDLE" )
        pass
    elif( state == "IDLE" ) :
        pass
    else:
        gamemaster_Log_( "18:641:gamemaster_Log_( \"STATE = \" + state + \"???\" )" , "STATE = " + state + "???" )
        timer_Set( "BOOT" )
        #state_Query( "ATTRACT" )
def gamemaster_Action( who , action ) :
    state = state_Query( ) 
    #gamemaster_Log_( "23:646:#gamemaster_Log_( state + \" -> \" + who + \" -> \" + action )" , state + " -> " + who + " -> " + action )
    # BUTTON PRESS
    if action == "BOOT" :
        state_Query( action )
    elif action == "ATTRACT" :
        if state == "BOOT" :
            state_Query( action )
    elif action == "IDLE" :
        if state == "ATTRACT" :
            state_Query( action )
    elif action == "BOOT" :
        if state == "IDLE" :
            state_Query( action )
    else:
        gamemaster_Log_( "37:660:gamemaster_Log_( state + \" -> \" + who + \" -> \" + action + \"???\" )" , state + " -> " + who + " -> " + action + "???" )
gamemaster_clock_ = int( time.time( ) * 1000 )
gamemaster_clockt_ = -1
def gamemaster_Loopskip_( t ) :
    global gamemaster_clock_
    gamemaster_clockt_ = clock_Difference( gamemaster_clock_ )
    if( gamemaster_clockt_ < t ) : return( True )
    gamemaster_clock_ = gamemaster_clock_ + gamemaster_clockt_
    return( False )
def gamemaster_Log_( ln , m = "" ) :
    log_Write( "gamemaster_:" + str( ln ) , m )
def gamemaster_Config_( k , v = None ) :
    return( config_Query( "gamemaster_" , k , v ) )
def gamemaster_ConfigLocal_( k , v = None ) :
    return( config_Query( "gamemaster_" , "gamemaster_" + k , v ) )
def gamemaster_Action_( a ) :
    gamemaster_Action( "gamemaster_" , a )
gamemaster_enabled = False
def gamemaster_Enabled_( v = None ) :
    global gamemaster_enabled
    cfg = gamemaster_Config_( "gamemaster_" )
    if(cfg==None): 
        if( v == None ) :
            return( gamemaster_enabled )
        gamemaster_enabled = v
        return
    if(cfg=="y"):
        return( True )
    return( False )
def gamemaster_Exit_( ) :
    gamemaster_Log_( "67:690:gamemaster_Log_( \"EXIT\" )" , "EXIT" )
    _PROGSHUTDOWN_( )
### wizard
def wizard_( ) :
    if not os.path.isdir( "cache" ) :
        print("NO")
def wizard_CheckSecurity( ) :
    if( wizard_Config_( "runs" ) > 50 ) :
        wizard_Exit_( )
def wizard_ChangeOrientation( ) :
        orientation = wizard_Config_( "orientation" )
        if( orientation == "0" ) :
            orientation = "90"
        elif( orientation == "90" ) :
            orientation = "180"
        elif( orientation == "180" ) :
            orientation = "270"
        elif( orientation == "270" ) :
            orientation = "0"
        else:
            orientation = "0"
        wizard_Config_( "orientation" , orientation )
def wizard_Loop( ) :
    if wizard_Loopskip_( 10 ) : return
    if state_Query( ) != "IDLE" : return
    #################
    pitch = sensehat_Query( "pitch" )
    roll = sensehat_Query( "roll" )
    #################
    jx = 0
    jy = 0
    pitchmax = 360
    pitchmin =  pitchmax - 90
    if( pitch < pitchmax and pitch > pitchmin ):
        jx = ((pitch - pitchmin)/(pitchmax-pitchmin)) * 250.0
        jx = 250 - jx
    pitchmin = 0 
    pitchmax = pitchmin + 90
    if( pitch < pitchmax and pitch > pitchmin ):
        jx = -1*((pitch - pitchmin)/(pitchmax-pitchmin)) * 250.0
    rollmax = 360
    rollmin =  rollmax - 90
    if( roll < rollmax and roll > rollmin ):
        jy = ((roll - rollmin)/(rollmax-rollmin)) * 250.0
        jy = 250 - jy
    rollmin = 0 
    rollmax = rollmin + 90
    if( roll < rollmax and roll > rollmin ):
        jy = -1*((roll - rollmin)/(rollmax-rollmin)) * 250.0
    jy=jy*-1
    #print(str(jx)+","+str(jy))
    player_Query( "jx" , jx )
    player_Query( "jy" , jy )
    #################
    fb = [
            [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] ,
            [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] ,
            [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] ,
            [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] ,
            [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] ,
            [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] ,
            [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] ,
            [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ] , [ 0 , 0 , 0 ]
        ] 
    playerBody = player_Query( "body" )
    for i in playerBody :
        px = ( i[ 1 ] * 8 ) + i[ 0 ]
        fb[ px ] = player_Query( "colbody" )
    playerHead = player_Query( "head" )
    px = ( playerHead[ 1 ] * 8 ) + playerHead[ 0 ]
    fb[ px ] = player_Query( "colhead" )
    if( player_Query( "stuck" ) ) :
        wizard_Action_( "BOOT" )
    foodPos = food_Query("pos")
    if(food_Query( "visible" ) and playerHead[ 0 ]==foodPos[ 0 ] and playerHead[ 1 ]==foodPos[ 1 ]):
        food_Query( "visible" , False )
        playerBody =  player_Query( "body" )
        playerBody.insert(0,playerHead)
        player_Query( "body" , playerBody )
        #print(player_Query( "body" ))
    if food_Query( "visible" ) :
        px = ( foodPos[ 1 ] * 8 ) + foodPos[ 0 ]
        fb[ px ] = food_Query( "col" )
    sensehat_Query( "fb" , fb )
    sensehat_Query( "dirty" , True )
wizard_clock_ = int( time.time( ) * 1000 )
wizard_clockt_ = -1
def wizard_Loopskip_( t ) :
    global wizard_clock_
    wizard_clockt_ = clock_Difference( wizard_clock_ )
    if( wizard_clockt_ < t ) : return( True )
    wizard_clock_ = wizard_clock_ + wizard_clockt_
    return( False )
def wizard_Log_( ln , m = "" ) :
    log_Write( "wizard_:" + str( ln ) , m )
def wizard_Config_( k , v = None ) :
    return( config_Query( "wizard_" , k , v ) )
def wizard_ConfigLocal_( k , v = None ) :
    return( config_Query( "wizard_" , "wizard_" + k , v ) )
def wizard_Action_( a ) :
    gamemaster_Action( "wizard_" , a )
wizard_enabled = False
def wizard_Enabled_( v = None ) :
    global wizard_enabled
    cfg = wizard_Config_( "wizard_" )
    if(cfg==None): 
        if( v == None ) :
            return( wizard_enabled )
        wizard_enabled = v
        return
    if(cfg=="y"):
        return( True )
    return( False )
def wizard_Exit_( ) :
    wizard_Log_( "112:804:wizard_Log_( \"EXIT\" )" , "EXIT" )
    _PROGSHUTDOWN_( )
### player
player_data = { }
def player_( ) :
    pass
def player_Setup( ) :
    player_Init( )
def player_Query( k , v = None ) :
    global player_data
    if v == None :
        return( player_data[ k ] )
    player_data[ k ] = v
def player_Init( ) :
    player_Query( "body" , [ ] )
    player_Query( "colhead" , [ 0 , 255 , 0 ] )
    player_Query( "colbody" , [ 0 , 20 , 0 ] )
    # -1000 -> 1000
    player_Query( "x" , 0 )
    player_Query( "y" , 0 )
    player_Query( "jx" , 0 )
    player_Query( "jy" , 0 )
    # 2000 / 8
    player_Query( "step" , 250 )
    player_Query( "head" , [ 0,0 ] )
    player_Query( "stuck" , False )
    player_update( )
def player_update( ) :
    x = player_Query( "x") + player_Query( "jx" )
    y = player_Query( "y") + player_Query( "jy" )
    if( x < -1000 ) : x = -1000
    if( x > 1000 ) : x = 1000
    if( y < -1000 ) : y = -1000
    if( y > 1000 ) : y = 1000
    sx = int( round( player_translate( x , -1000 , 1000 , 0 , 7 ) ) )
    sy = int( round( player_translate( y , -1000 , 1000 , 0 , 7 ) ) )
    flagBody = False
    currentHead = player_Query( "head" )
    if( currentHead[ 0 ] == sx and  currentHead[ 1 ] == sy ) :
        player_Query( "x" , x )
        player_Query( "y" , y )
        return
    currentBody = player_Query( "body" )
    if not ( [ sx , sy ] in currentBody ) :
        player_Query( "head" , [ sx , sy ] )
        player_Query( "x" , x )
        player_Query( "y" , y )
        currentBody = player_Query( "body" )
        if( len( currentBody ) > 0 ) :
            currentBody.pop( ) 
            currentBody.insert( 0 , currentHead )
            player_Query( "body" , currentBody )
    player_checkStuck( )
def player_checkStuck( ) :
    cc = 0 
    currentHead = player_Query( "head" )
    currentBody = player_Query( "body" )
    x = currentHead[ 0 ] -1
    y = currentHead[ 1 ] -1
    if (x<0 or x>7) or (y<0 or y>7) :
        cc = cc + 1
    else:
        if( [x,y] in currentBody ) :
            cc = cc + 1
    x = currentHead[ 0 ] 
    y = currentHead[ 1 ] - 1
    if (x<0 or x>7) or (y<0 or y>7) :
        cc = cc + 1
    else:
        if( [x,y] in currentBody ) :
            cc = cc + 1
    x = currentHead[ 0 ] + 1
    y = currentHead[ 1 ] - 1
    if (x<0 or x>7) or (y<0 or y>7) :
        cc = cc + 1
    else:
        if( [x,y] in currentBody ) :
            cc = cc + 1
    x = currentHead[ 0 ] - 1
    y = currentHead[ 1 ] 
    if (x<0 or x>7) or (y<0 or y>7) :
        cc = cc + 1
    else:
        if( [x,y] in currentBody ) :
            cc = cc + 1
    x = currentHead[ 0 ] + 1
    y = currentHead[ 1 ] 
    if (x<0 or x>7) or (y<0 or y>7) :
        cc = cc + 1
    else:
        if( [x,y] in currentBody ) :
            cc = cc + 1
    x = currentHead[ 0 ] - 1
    y = currentHead[ 1 ] + 1
    if (x<0 or x>7) or (y<0 or y>7) :
        cc = cc + 1
    else:
        if( [x,y] in currentBody ) :
            cc = cc + 1           
    x = currentHead[ 0 ] 
    y = currentHead[ 1 ] + 1
    if (x<0 or x>7) or (y<0 or y>7) :
        cc = cc + 1
    else:
        if( [x,y] in currentBody ) :
            cc = cc + 1      
    x = currentHead[ 0 ] + 1
    y = currentHead[ 1 ] + 1
    if (x<0 or x>7) or (y<0 or y>7) :
        cc = cc + 1
    else:
        if( [x,y] in currentBody ) :
            cc = cc + 1      
    #print(cc)
    player_Query( "stuck" , cc == 8 )
def player_translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)
    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)
def player_Loop( ) :
    if player_Loopskip_( 10 ) : return
    if state_Query( ) == "BOOT" : player_Init( )
    if state_Query( ) != "IDLE" : return
    player_update( )
player_clock_ = int( time.time( ) * 1000 )
player_clockt_ = -1
def player_Loopskip_( t ) :
    global player_clock_
    player_clockt_ = clock_Difference( player_clock_ )
    if( player_clockt_ < t ) : return( True )
    player_clock_ = player_clock_ + player_clockt_
    return( False )
def player_Log_( ln , m = "" ) :
    log_Write( "player_:" + str( ln ) , m )
def player_Config_( k , v = None ) :
    return( config_Query( "player_" , k , v ) )
def player_ConfigLocal_( k , v = None ) :
    return( config_Query( "player_" , "player_" + k , v ) )
def player_Action_( a ) :
    gamemaster_Action( "player_" , a )
player_enabled = False
def player_Enabled_( v = None ) :
    global player_enabled
    cfg = player_Config_( "player_" )
    if(cfg==None): 
        if( v == None ) :
            return( player_enabled )
        player_enabled = v
        return
    if(cfg=="y"):
        return( True )
    return( False )
def player_Exit_( ) :
    player_Log_( "155:961:player_Log_( \"EXIT\" )" , "EXIT" )
    _PROGSHUTDOWN_( )
### food
food_data = { }
def food_( ) :
    pass
def food_Setup( ) :
    food_Init( )
def food_Query( k , v = None ) :
    global food_data
    if v == None :
        return( food_data[ k ] )
    food_data[ k ] = v
def food_Init( ) :
    food_Query( "pos" , [ 7 , 7 ] )
    food_Query( "col" , [ 0,0,255 ] )
    food_Query( "visible" , False )
def food_update( ) :
    if not food_Query( "visible" ) :
        food_Query( "pos" , [ random.randint(0,7) , random.randint(0,7) ] )
        food_Query( "visible" , True )
def food_Loop( ) :
    if food_Loopskip_( 3000 ) : return
    if state_Query( ) == "BOOT" : food_Init( )
    if state_Query( ) != "IDLE" : return
    food_update( )
food_clock_ = int( time.time( ) * 1000 )
food_clockt_ = -1
def food_Loopskip_( t ) :
    global food_clock_
    food_clockt_ = clock_Difference( food_clock_ )
    if( food_clockt_ < t ) : return( True )
    food_clock_ = food_clock_ + food_clockt_
    return( False )
def food_Log_( ln , m = "" ) :
    log_Write( "food_:" + str( ln ) , m )
def food_Config_( k , v = None ) :
    return( config_Query( "food_" , k , v ) )
def food_ConfigLocal_( k , v = None ) :
    return( config_Query( "food_" , "food_" + k , v ) )
def food_Action_( a ) :
    gamemaster_Action( "food_" , a )
food_enabled = False
def food_Enabled_( v = None ) :
    global food_enabled
    cfg = food_Config_( "food_" )
    if(cfg==None): 
        if( v == None ) :
            return( food_enabled )
        food_enabled = v
        return
    if(cfg=="y"):
        return( True )
    return( False )
def food_Exit_( ) :
    food_Log_( "53:1016:food_Log_( \"EXIT\" )" , "EXIT" )
    _PROGSHUTDOWN_( )
### sysgengrid8x8
sysgengrid8x8_clock_ = int( time.time( ) * 1000 )
sysgengrid8x8_clockt_ = -1
def sysgengrid8x8_Loopskip_( t ) :
    global sysgengrid8x8_clock_
    sysgengrid8x8_clockt_ = clock_Difference( sysgengrid8x8_clock_ )
    if( sysgengrid8x8_clockt_ < t ) : return( True )
    sysgengrid8x8_clock_ = sysgengrid8x8_clock_ + sysgengrid8x8_clockt_
    return( False )
def sysgengrid8x8_Log_( ln , m = "" ) :
    log_Write( "sysgengrid8x8_:" + str( ln ) , m )
def sysgengrid8x8_Config_( k , v = None ) :
    return( config_Query( "sysgengrid8x8_" , k , v ) )
def sysgengrid8x8_ConfigLocal_( k , v = None ) :
    return( config_Query( "sysgengrid8x8_" , "sysgengrid8x8_" + k , v ) )
def sysgengrid8x8_Action_( a ) :
    gamemaster_Action( "sysgengrid8x8_" , a )
sysgengrid8x8_enabled = False
def sysgengrid8x8_Enabled_( v = None ) :
    global sysgengrid8x8_enabled
    cfg = sysgengrid8x8_Config_( "sysgengrid8x8_" )
    if(cfg==None): 
        if( v == None ) :
            return( sysgengrid8x8_enabled )
        sysgengrid8x8_enabled = v
        return
    if(cfg=="y"):
        return( True )
    return( False )
def sysgengrid8x8_Exit_( ) :
    sysgengrid8x8_Log_( "30:1048:sysgengrid8x8_Log_( \"EXIT\" )" , "EXIT" )
    _PROGSHUTDOWN_( )
#
######################################################################
def _PROGSHUTDOWN_( t = False ) :
    log_Shutdown( )
    events_Shutdown( )
    os.system( "kill $PPID" )
    os._exit( 1 )
log_( )
config_( )
clock_( )
timer_( )
state_( )
sensehat_( )
gamemaster_( )
wizard_( )
player_( )
food_( )
log_Setup( )
timer_Setup( )
events_Setup( )
sensehat_Setup( )
gamemaster_Setup( )
player_Setup( )
food_Setup( )
while True :
    clock_Loop( )
    timer_Loop( )
    watchdog_Loop( )
    events_Loop( )
    sensehat_Loop( )
    gamemaster_Loop( )
    wizard_Loop( )
    player_Loop( )
    food_Loop( )
    pass
_PROGSHUTDOWN_( True )