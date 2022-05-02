#############################################################################
# Generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#  May 02, 2022 11:16:11 AM PDT  platform: Linux
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
    wm geometry $top 943x450+424+329
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
    vTcl:DefineAlias "$top" "VehicleSearchForm" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    vTcl::widgets::ttk::custom::CreateCmd $top.cus46 \
        -background $vTcl(actual_gui_bg) -height 258 -highlightcolor black \
        -width 916 
    vTcl:DefineAlias "$top.cus46" "Custom1" vTcl:WidgetProc "VehicleSearchForm" 1
    menu $top.m51 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tLa47 \
        -text {Enter Vehicle Search Criteria} -relief solid -width 920 \
        -height 165 
    vTcl:DefineAlias "$top.tLa47" "TLabelframe1" vTcl:WidgetProc "VehicleSearchForm" 1
    set site_3_0 $top.tLa47
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu48 \
        -command do_vehicle_search -takefocus {} -text Search -compound left 
    vTcl:DefineAlias "$site_3_0.tBu48" "TButton1" vTcl:WidgetProc "VehicleSearchForm" 1
    ttk::entry $site_3_0.tEn49 \
        -font TkTextFont -textvariable yearValue -foreground {} \
        -background {} -takefocus {} -cursor xterm 
    vTcl:DefineAlias "$site_3_0.tEn49" "Year" vTcl:WidgetProc "VehicleSearchForm" 1
    ttk::entry $site_3_0.tEn50 \
        -font TkTextFont -textvariable makeValue -foreground {} \
        -background {} -takefocus {} -cursor xterm 
    vTcl:DefineAlias "$site_3_0.tEn50" "Make" vTcl:WidgetProc "VehicleSearchForm" 1
    ttk::entry $site_3_0.tEn51 \
        -font TkTextFont -textvariable colorValue -foreground {} \
        -background {} -takefocus {} -cursor xterm 
    vTcl:DefineAlias "$site_3_0.tEn51" "Color" vTcl:WidgetProc "VehicleSearchForm" 1
    ttk::label $site_3_0.tLa52 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left -text Year \
        -compound left 
    vTcl:DefineAlias "$site_3_0.tLa52" "TLabel1" vTcl:WidgetProc "VehicleSearchForm" 1
    ttk::label $site_3_0.tLa53 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left -text Make \
        -compound left 
    vTcl:DefineAlias "$site_3_0.tLa53" "TLabel1_1" vTcl:WidgetProc "VehicleSearchForm" 1
    ttk::label $site_3_0.tLa54 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left -text Color \
        -compound left 
    vTcl:DefineAlias "$site_3_0.tLa54" "TLabel1_1_1" vTcl:WidgetProc "VehicleSearchForm" 1
    ttk::entry $site_3_0.tEn57 \
        -font TkTextFont -textvariable modelValue -foreground {} \
        -background {} -takefocus {} -cursor xterm 
    vTcl:DefineAlias "$site_3_0.tEn57" "ModelEntry" vTcl:WidgetProc "VehicleSearchForm" 1
    ttk::label $site_3_0.tLa58 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left -text Model \
        -compound left 
    vTcl:DefineAlias "$site_3_0.tLa58" "TLabel4" vTcl:WidgetProc "VehicleSearchForm" 1
    ttk::entry $site_3_0.tEn59 \
        -font TkTextFont -textvariable milesValue -foreground {} \
        -background {} -takefocus {} -cursor xterm 
    vTcl:DefineAlias "$site_3_0.tEn59" "MilesEnty" vTcl:WidgetProc "VehicleSearchForm" 1
    ttk::label $site_3_0.tLa60 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font TkDefaultFont -relief flat -anchor w -justify left -text Miles \
        -compound left 
    vTcl:DefineAlias "$site_3_0.tLa60" "TLabel4" vTcl:WidgetProc "VehicleSearchForm" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu61 \
        -command clearButtonClick -takefocus {} -text Clear -compound left 
    vTcl:DefineAlias "$site_3_0.tBu61" "TButton2" vTcl:WidgetProc "VehicleSearchForm" 1
    place $site_3_0.tBu48 \
        -in $site_3_0 -x 830 -y 130 -anchor nw -bordermode ignore 
    place $site_3_0.tEn49 \
        -in $site_3_0 -x 150 -y 30 -anchor nw -bordermode ignore 
    place $site_3_0.tEn50 \
        -in $site_3_0 -x 150 -y 60 -anchor nw -bordermode ignore 
    place $site_3_0.tEn51 \
        -in $site_3_0 -x 420 -y 30 -anchor nw -bordermode ignore 
    place $site_3_0.tLa52 \
        -in $site_3_0 -x 20 -y 30 -anchor nw -bordermode ignore 
    place $site_3_0.tLa53 \
        -in $site_3_0 -x 20 -y 60 -width 46 -height 26 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tLa54 \
        -in $site_3_0 -x 370 -y 30 -width 46 -height 26 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tEn57 \
        -in $site_3_0 -x 150 -y 90 -width 164 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tLa58 \
        -in $site_3_0 -x 20 -y 90 -anchor nw -bordermode ignore 
    place $site_3_0.tEn59 \
        -in $site_3_0 -x 150 -y 120 -width 164 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tLa60 \
        -in $site_3_0 -x 20 -y 120 -anchor nw -bordermode ignore 
    place $site_3_0.tBu61 \
        -in $site_3_0 -x 740 -y 130 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.cus46 \
        -in $top -x 10 -y 180 -width 916 -relwidth 0 -height 258 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa47 \
        -in $top -x 10 -y 10 -width 920 -relwidth 0 -height 165 -relheight 0 \
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
Window show .top2 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

