#############################################################################
# Generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#  May 03, 2022 01:06:19 PM PDT  platform: Linux
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
        -menu {{}} -background $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 792x757+512+418
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
    set toptitle "Add Customer Payment Form"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "AddCustomerPaymentForm" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    label $top.lab46 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Select a customer to enter payments:} 
    vTcl:DefineAlias "$top.lab46" "SelectACustomer" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    label $top.lab47 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Customer 
    vTcl:DefineAlias "$top.lab47" "Customer" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    label $top.lab51 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Payment History} 
    vTcl:DefineAlias "$top.lab51" "Label1" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    label $top.lab53 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Payment Date} 
    vTcl:DefineAlias "$top.lab53" "PaymentDate" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    label $top.lab54 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Amount Due} 
    vTcl:DefineAlias "$top.lab54" "Due" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    label $top.lab55 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Paid Date} 
    vTcl:DefineAlias "$top.lab55" "PaidDate" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    label $top.lab56 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Amount 
    vTcl:DefineAlias "$top.lab56" "Amount" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    label $top.lab57 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Bank Account} 
    vTcl:DefineAlias "$top.lab57" "BankAmount" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    button $top.but63 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -command AddPayment -compound left \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -pady 0 -text Add 
    vTcl:DefineAlias "$top.but63" "AddMore" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    entry $top.ent64 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable paymentDueValue -width 134 
    vTcl:DefineAlias "$top.ent64" "PaymentDateEntry" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    entry $top.ent65 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable amountDueValue -width 104 
    vTcl:DefineAlias "$top.ent65" "DueEntry" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    entry $top.ent66 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable paidDateValue -width 124 
    vTcl:DefineAlias "$top.ent66" "PaidDateEntry" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    entry $top.ent67 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable amuntPaidValue -width 94 
    vTcl:DefineAlias "$top.ent67" "AmountEntry" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    entry $top.ent68 \
        -background white -font TkFixedFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black -insertbackground black -selectbackground blue \
        -selectforeground white -textvariable bankAccountValue -width 114 
    vTcl:DefineAlias "$top.ent68" "BankAmountEntry" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    vTcl::widgets::ttk::custom::CreateCmd $top.cus69 \
        -background $vTcl(actual_gui_bg) -height 75 -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$top.cus69" "Custom1" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    ttk::combobox $top.tCo79 \
        -font TkTextFont -textvariable customerValue -foreground {} \
        -background {} -takefocus {} 
    vTcl:DefineAlias "$top.tCo79" "CustomerComboBox" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    vTcl::widgets::ttk::custom::CreateCmd $top.cus80 \
        -background $vTcl(actual_gui_bg) -height 75 -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$top.cus80" "Custom4" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    ttk::separator $top.tSe81
    vTcl:DefineAlias "$top.tSe81" "TSeparator3" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    ttk::label $top.tLa82 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font {-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -relief flat -anchor w -justify left -text {Add Customer Payment} \
        -compound left 
    vTcl:DefineAlias "$top.tLa82" "TLabel4" vTcl:WidgetProc "AddCustomerPaymentForm" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab46 \
        -in $top -x 11 -y 14 -width 426 -relwidth 0 -height 28 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 20 -y 50 -width 105 -relwidth 0 -height 29 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab51 \
        -in $top -x 0 -y 259 -width 193 -relwidth 0 -height 29 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab53 \
        -in $top -x 10 -y 150 -width 145 -relwidth 0 -height 28 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab54 \
        -in $top -x 180 -y 150 -width 111 -relwidth 0 -height 28 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab55 \
        -in $top -x 290 -y 140 -width 105 -relwidth 0 -height 28 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab56 \
        -in $top -x 430 -y 140 -width 105 -relwidth 0 -height 28 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab57 \
        -in $top -x 540 -y 140 -width 105 -relwidth 0 -height 28 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but63 \
        -in $top -x 680 -y 180 -width 107 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent64 \
        -in $top -x 10 -y 180 -width 134 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent65 \
        -in $top -x 170 -y 180 -width 104 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent66 \
        -in $top -x 290 -y 180 -width 124 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent67 \
        -in $top -x 430 -y 180 -width 94 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent68 \
        -in $top -x 540 -y 180 -width 114 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.cus69 \
        -in $top -x 11 -y 459 -width 770 -relwidth 0 -height 288 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tCo79 \
        -in $top -x 144 -y 54 -width 285 -relwidth 0 -height 26 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.cus80 \
        -in $top -x 11 -y 285 -width 771 -relwidth 0 -height 156 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tSe81 \
        -in $top -x 10 -y 110 -width 770 -relwidth 0 -anchor nw \
        -bordermode ignore 
    place $top.tLa82 \
        -in $top -x 10 -y 120 -anchor nw -bordermode ignore 
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

