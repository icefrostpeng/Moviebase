#############################################################################
# Generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#  Mar 24, 2021 09:14:45 AM IST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


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




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m49" -background #000040 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor #000000 
    wm focusmodel $top passive
    wm geometry $top 1280x686+212+135
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 3004 1913
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Search" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    menu $top.m49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    label $top.lab78 \
        -activebackground #f9f9f9 -activeforeground black -background #000040 \
        -borderwidth 5 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 22 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text Recommended! 
    vTcl:DefineAlias "$top.lab78" "Recommended_l" vTcl:WidgetProc "Search" 1
    ttk::separator $top.tSe97 \
        -orient vertical 
    vTcl:DefineAlias "$top.tSe97" "TSeparator3" vTcl:WidgetProc "Search" 1
    ttk::separator $top.tSe100 \
        -orient vertical 
    vTcl:DefineAlias "$top.tSe100" "TSeparator4" vTcl:WidgetProc "Search" 1
    frame $top.fra48 \
        -borderwidth 2 -relief groove -background #00002b -height 95 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 795 
    vTcl:DefineAlias "$top.fra48" "Movie1" vTcl:WidgetProc "Search" 1
    set site_3_0 $top.fra48
    label $site_3_0.lab50 \
        -activebackground #f9f9f9 -activeforeground black -anchor nw \
        -background #00002b -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #bcfbfe -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {Name of cinema with address} 
    vTcl:DefineAlias "$site_3_0.lab50" "Description1" vTcl:WidgetProc "Search" 1
    label $site_3_0.lab48 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -text timings 
    vTcl:DefineAlias "$site_3_0.lab48" "Label3" vTcl:WidgetProc "Search" 1
    label $site_3_0.lab49 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -text timings 
    vTcl:DefineAlias "$site_3_0.lab49" "Label4" vTcl:WidgetProc "Search" 1
    place $site_3_0.lab50 \
        -in $site_3_0 -x 0 -relx 0.025 -y 0 -rely 0.106 -width 0 \
        -relwidth 0.961 -height 0 -relheight 0.34 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 0 -relx 0.038 -y 0 -rely 0.638 -width 0 \
        -relwidth 0.068 -height 0 -relheight 0.223 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 0 -relx 0.138 -y 0 -rely 0.638 -width 0 \
        -relwidth 0.069 -height 0 -relheight 0.223 -anchor nw \
        -bordermode ignore 
    button $top.but51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #b4eafe -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text < 
    vTcl:DefineAlias "$top.but51" "Previous" vTcl:WidgetProc "Search" 1
    vTcl:copy_lock $top.but51
    button $top.but52 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #b4eafe -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text > 
    vTcl:DefineAlias "$top.but52" "Next" vTcl:WidgetProc "Search" 1
    vTcl:copy_lock $top.but52
    label $top.lab53 \
        -activebackground #f0f0f0f0f0f0 -activeforeground black \
        -background #000040 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #b4eafe -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {1 of 4} 
    vTcl:DefineAlias "$top.lab53" "Page_list" vTcl:WidgetProc "Search" 1
    label $top.lab45 \
        -background #000040 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #bbfcff -text Date 
    vTcl:DefineAlias "$top.lab45" "Label2" vTcl:WidgetProc "Search" 1
    button $top.but46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #5bedf9 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 18 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text < 
    vTcl:DefineAlias "$top.but46" "Button1" vTcl:WidgetProc "Search" 1
    button $top.but47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #5bedf9 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 18 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text > 
    vTcl:DefineAlias "$top.but47" "Button2" vTcl:WidgetProc "Search" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab78 \
        -in $top -x 0 -relx 0.172 -y 0 -rely 0.131 -width 0 -relwidth 0.159 \
        -height 0 -relheight 0.07 -anchor nw -bordermode ignore 
    place $top.tSe97 \
        -in $top -x 0 -relx 0.165 -y 0 -rely 0.167 -width 0 -relwidth 0.001 \
        -height 0 -relheight 0.846 -anchor nw -bordermode inside 
    place $top.tSe100 \
        -in $top -x 0 -relx 0.818 -y 0 -rely 0.167 -width 0 -relwidth 0.001 \
        -height 0 -relheight 0.836 -anchor nw -bordermode inside 
    place $top.fra48 \
        -in $top -x 0 -relx 0.18 -y 0 -rely 0.364 -width 0 -relwidth 0.621 \
        -height 0 -relheight 0.137 -anchor nw -bordermode ignore 
    place $top.but51 \
        -in $top -x 0 -relx 0.383 -y 0 -rely 0.933 -width 47 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but52 \
        -in $top -x 0 -relx 0.57 -y 0 -rely 0.933 -width 47 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab53 \
        -in $top -x 0 -relx 0.43 -y 0 -rely 0.933 -width 0 -relwidth 0.128 \
        -height 0 -relheight 0.031 -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 0 -relx 0.461 -y 0 -rely 0.248 -width 0 -relwidth 0.058 \
        -height 0 -relheight 0.074 -anchor nw -bordermode ignore 
    place $top.but46 \
        -in $top -x 0 -relx 0.391 -y 0 -rely 0.262 -width 47 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 0 -relx 0.555 -y 0 -rely 0.262 -width 47 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

