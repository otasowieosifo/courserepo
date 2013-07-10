# Stopwatch using simplegui.
# Pyhton code designed by Otasowie Osifo as part of the assignments in the course: Interactive Python.
# This file should be loaded into codeskulptor at www.codeskulptor.org

import simplegui
import math

#Global variables that are used for communication and synchronization.
gbl_seconds_counter = 0
gbl_timer_scaler = 0.1
gbl_out_str = "0:00.0"
gbl_timer_interval = 100
gbl_timer = None
gbl_integral_stops_counter = 0
gbl_total_stops_counter = 0
gbl_stops_str = "0/0"
gbl_timer_is_runing = 0 


# define helper function: format_string that converts time
# in tenths of seconds into formatted string A:BC.D
def format_string( t ):
    global gbl_out_str
    decimal_value = t * gbl_timer_scaler
    value = math.floor( decimal_value )
    diff = decimal_value - value
    diff = diff * 10
    diff = round( diff, 1 )
    decimal_str = "." + str( diff )
    remainder = int( value ) % 60
    if value >= 60:
        minutes = value  / 60
        minutes = math.floor( minutes )
    else:
        minutes = 0
    minutes_str = str( minutes )
    if remainder < 10:
        second_str = "0" + str( remainder )
    else:
        second_str = str( remainder )
    out_str = second_str + decimal_str
    gbl_out_str = minutes_str + ":" + out_str
        
# event handler for the timer process
def handle_timer_event():
    global gbl_seconds_counter
    global gbl_timer_in_seconds
    gbl_seconds_counter = gbl_seconds_counter + 1
    format_string( gbl_seconds_counter )
    
#Helper function to the event handler for the start button    
def handle_timer():
    global gbl_timer
    global gbl_timer_is_runing
    bool( gbl_timer_is_runing )
    if  gbl_timer_is_runing == False:
        if gbl_timer == None:
            gbl_timer = simplegui.create_timer( gbl_timer_interval, handle_timer_event)
        gbl_timer.start()
        gbl_timer_is_runing = 1

#Event handler for the start button     
def start_stop_watch():
        handle_timer()

#Event handler for the stop button
def stop_stop_watch():
    if gbl_timer != None:
        gbl_timer.stop()
        global gbl_integral_stops_counter
        global gbl_total_stops_counter
        global gbl_stops_str
        global gbl_timer_is_runing
        bool( gbl_timer_is_runing )
        if gbl_timer_is_runing == True:
             gbl_total_stops_counter = gbl_total_stops_counter + 1
             if gbl_seconds_counter % 10 == 0:
                    gbl_integral_stops_counter = gbl_integral_stops_counter + 1
             gbl_stops_str = str(gbl_integral_stops_counter) + "/" + str(gbl_total_stops_counter)
        gbl_timer_is_runing = 0

#Event handlar fro the stop button        
def reset_stop_watch():
    global gbl_seconds_counter
    global gbl_integral_stops_counter
    global gbl_total_stops_counter
    global gbl_stops_str
    global gbl_out_str
    gbl_integral_stops_counter = 0
    gbl_total_stops_counter = 0
    gbl_stops_str = "0/0"
    gbl_out_str = "0:00.0"
    gbl_seconds_counter = 0
    if gbl_timer != None:
        gbl_timer.stop()
        global gbl_timer_is_runing
        gbl_timer_is_runing = 0
    
    
# Draw text to canvas
def draw_text_to_canvas(canvas):
    canvas.draw_text( gbl_stops_str, ( 160, 16), 16, "Lime")
    canvas.draw_text( gbl_out_str, ( 35, 110), 30, "Lime")
    
    
# Module for graphics
def handle_gui_frame():
    gframe = simplegui.create_frame( "Electronic Stop Watch", 200, 200)
    gframe.set_draw_handler(draw_text_to_canvas)
    gframe.add_button( "Start", start_stop_watch, 150)
    gframe.add_button( "Stop", stop_stop_watch, 150)
    gframe.add_button( "Reset", reset_stop_watch, 150)
    gframe.start()

#The main function for starting the gui
def stop_watch_main():
    handle_gui_frame()
    
#Start the stopwatch
stop_watch_main()


    

# Please remember to review the grading rubric

