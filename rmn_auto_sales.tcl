#############################################################################
# Generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#  Apr 14, 2022 09:19:14 AM PDT  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Absolute
}




proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m50" -background $vTcl(actual_gui_bg) \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+1896+333
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 3825 2130
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "RMN Auto Sales - Home"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "HomePage" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    button $top.but47 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 \
        -command button_click_purchase_car -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Purchase Car} 
    vTcl:DefineAlias "$top.but47" "purchase_car_button" vTcl:WidgetProc "HomePage" 1
    button $top.but48 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -compound left \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text {Sell Car} 
    vTcl:DefineAlias "$top.but48" "sell_car_button" vTcl:WidgetProc "HomePage" 1
    button $top.but49 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 -compound left \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -text {Sell Warranty} 
    vTcl:DefineAlias "$top.but49" "sell_warranty_button" vTcl:WidgetProc "HomePage" 1
    menu $top.m50 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    button $top.but50 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -borderwidth 2 \
        -command button_vehicle_search -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Vehicle Search} 
    vTcl:DefineAlias "$top.but50" "purchase_car_button_1" vTcl:WidgetProc "HomePage" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but47 \
        -in $top -x 20 -y 40 -width 158 -relwidth 0 -height 120 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but48 \
        -in $top -x 210 -y 40 -width 158 -relwidth 0 -height 120 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 400 -y 40 -width 158 -relwidth 0 -height 120 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but50 \
        -in $top -x 20 -y 220 -width 158 -height 120 -anchor nw \
        -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

proc vTclWindow.top2 {base} {
    global vTcl
    if {$base == ""} {
        set base .top2
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m51" -background $vTcl(actual_gui_bg) \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+1885+815
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 3825 2130
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Vehicle Search"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "vehicle_search" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    vTcl::widgets::ttk::custom::CreateCmd $top.cus46 \
        -background $vTcl(actual_gui_bg) -height 75 -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$top.cus46" "Custom1" vTcl:WidgetProc "vehicle_search" 1
    menu $top.m51 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.cus46 \
        -in $top -x 10 -y 260 -width 586 -relwidth 0 -height 168 -relheight 0 \
        -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}
set btop2 ""
if {$vTcl(borrow)} {
    set btop2 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop2 $vTcl(tops)] != -1} {
        set btop2 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop2
Window show .top2 $btop2
if {$vTcl(borrow)} {
    $btop2 configure -background plum
}

