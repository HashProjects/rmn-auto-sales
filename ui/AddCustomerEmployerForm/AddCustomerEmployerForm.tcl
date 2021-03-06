#############################################################################
# Generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#  Apr 27, 2022 07:36:17 PM PDT  platform: Linux
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
set vTcl(mode) Relative
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
        -menu "$top.m51" -background $vTcl(actual_gui_bg) \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x441+1786+883
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Add Employer Information"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    label $top.lab46 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Employer Information} 
    vTcl:DefineAlias "$top.lab46" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab47 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Company 
    vTcl:DefineAlias "$top.lab47" "Company" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab48 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Address 
    vTcl:DefineAlias "$top.lab48" "Address" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab49 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text State 
    vTcl:DefineAlias "$top.lab49" "State" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab50 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text Superviser 
    vTcl:DefineAlias "$top.lab50" "Superviser" vTcl:WidgetProc "Toplevel1" 1
    menu $top.m51 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    label $top.lab52 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {State Date} 
    vTcl:DefineAlias "$top.lab52" "Superviser_1" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent53 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable employerValue -width 154 
    vTcl:DefineAlias "$top.ent53" "CompanyEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent54 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable addressValue -width 154 
    vTcl:DefineAlias "$top.ent54" "AddressEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent55 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable stateValue -width 154 
    vTcl:DefineAlias "$top.ent55" "StateEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent56 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable supervisorValue -width 154 
    vTcl:DefineAlias "$top.ent56" "SuperviserEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent57 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable startDateValue -width 154 
    vTcl:DefineAlias "$top.ent57" "StartDateEntry" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab58 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Title 
    vTcl:DefineAlias "$top.lab58" "Title" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab59 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text City 
    vTcl:DefineAlias "$top.lab59" "City" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab60 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Zip 
    vTcl:DefineAlias "$top.lab60" "Zip" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab61 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Phone 
    vTcl:DefineAlias "$top.lab61" "Phone" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab62 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {End Date} 
    vTcl:DefineAlias "$top.lab62" "EndDate" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent63 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable titleValue -width 154 
    vTcl:DefineAlias "$top.ent63" "TitleEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent64 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable cityValue -width 154 
    vTcl:DefineAlias "$top.ent64" "CityEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent65 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable zipValue -width 154 
    vTcl:DefineAlias "$top.ent65" "ZipEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent66 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable phoneValue -width 154 
    vTcl:DefineAlias "$top.ent66" "PhoneEntry" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent68 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable endDateValue -width 154 
    vTcl:DefineAlias "$top.ent68" "EndDateEntry" vTcl:WidgetProc "Toplevel1" 1
    button $top.but69 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command Submit -compound left \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -pady 0 -text Submit 
    vTcl:DefineAlias "$top.but69" "Submit" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu46 \
        -command randomData -takefocus {} -text Random -compound left 
    vTcl:DefineAlias "$top.tBu46" "Random" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab46 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.022 -width 0 -relwidth 0.29 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.133 -width 0 -relwidth 0.19 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.244 -width 0 -relwidth 0.19 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.356 -width 0 -relwidth 0.19 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab50 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.467 -width 0 -relwidth 0.19 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.578 -width 0 -relwidth 0.19 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.ent53 \
        -in $top -x 0 -relx 0.217 -y 0 -rely 0.133 -width 154 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent54 \
        -in $top -x 0 -relx 0.217 -y 0 -rely 0.244 -width 154 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent55 \
        -in $top -x 0 -relx 0.217 -y 0 -rely 0.356 -width 154 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent56 \
        -in $top -x 0 -relx 0.217 -y 0 -rely 0.467 -width 154 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent57 \
        -in $top -x 0 -relx 0.217 -y 0 -rely 0.578 -width 154 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab58 \
        -in $top -x 0 -relx 0.533 -y 0 -rely 0.133 -width 0 -relwidth 0.19 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab59 \
        -in $top -x 0 -relx 0.533 -y 0 -rely 0.244 -width 0 -relwidth 0.19 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab60 \
        -in $top -x 0 -relx 0.533 -y 0 -rely 0.356 -width 0 -relwidth 0.19 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab61 \
        -in $top -x 0 -relx 0.533 -y 0 -rely 0.467 -width 0 -relwidth 0.19 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab62 \
        -in $top -x 0 -relx 0.533 -y 0 -rely 0.578 -width 0 -relwidth 0.19 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.ent63 \
        -in $top -x 0 -relx 0.717 -y 0 -rely 0.133 -width 154 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent64 \
        -in $top -x 0 -relx 0.717 -y 0 -rely 0.244 -width 154 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent65 \
        -in $top -x 0 -relx 0.717 -y 0 -rely 0.356 -width 154 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent66 \
        -in $top -x 0 -relx 0.717 -y 0 -rely 0.467 -width 154 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.ent68 \
        -in $top -x 0 -relx 0.717 -y 0 -rely 0.578 -width 154 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but69 \
        -in $top -x 0 -relx 0.75 -y 0 -rely 0.93 -width 147 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $top.tBu46 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.907 -width 83 -relwidth 0 \
        -height 28 -relheight 0 -anchor nw -bordermode ignore 
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

