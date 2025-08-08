#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: gnuradio
# GNU Radio version: 3.10.10.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio import fec
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import soapy
import sip
import test9_epy_block_0_1_0 as epy_block_0_1_0  # embedded python block


def snipfcn_snippet_0(self):
    ##def convert_to_tmp(input_file, output_file, header_string, footer_string):
    ##    """
    ##    Converts a file to .tmp format by copying its content, adding a header at the beginning,
    ##    and a footer at the end.
    ##
    ##    Args:
    ##        input_file (str): Path to the input file.
    ##        output_file (str): Path to save the .tmp file.
    ##        header_string (str): Header string to add at the beginning of the .tmp file.
    ##        footer_string (str): Footer string to add at the end of the .tmp file.
    ##
    ##    Returns:
    ##        str: Path to the created .tmp file.
    ##    """
    ####    if not os.path.isfile(input_file):
    ####        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")
    ####
    ####    # Ensure the output directory exists
    ####    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    ####
    ##    # Read the content of the input file
    ##    with open(input_file, 'rb') as infile:
    ##        content = infile.read()
    ##
    ##    # Write the header, content, and footer to the .tmp file
    ##    with open(output_file, 'wb') as outfile:
    ##        outfile.write(header_string.encode('utf-8') + b"\n")  # Write the header
    ##        outfile.write(content)                                 # Write the file content
    ##        outfile.write(b"\n" + footer_string.encode('utf-8'))  # Write the footer
    ##
    ##    return output_file

    def convert_tmp_to_original(tmp_file, original_extension, output_file, header_end_marker, footer_start_marker):
        """
        Converts a .tmp file back to its original format by removing the header and footer strings
        and renaming it with the provided extension.

        Args:
            tmp_file (str): Path to the .tmp file.
            original_extension (str): Original file extension (e.g., '.txt', '.jpg').
            output_file (str): Path to save the restored file.
            header_end_marker (str): Unique string at the end of the header to identify its boundary.
            footer_start_marker (str): Unique string at the start of the footer to identify its boundary.

        Returns:
            str: Path to the restored original file.
        """
    ##    if not os.path.isfile(tmp_file):
    ##        raise FileNotFoundError(f"Temporary file '{tmp_file}' does not exist.")

    ##    # Ensure the output directory exists
    ##    os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Read the content of the .tmp file
        with open(tmp_file, 'rb') as infile:
            content = infile.read()

        # Find the header end marker and remove the header
        header_end_marker_bytes = header_end_marker.encode('utf-8')
        header_end_index = content.find(header_end_marker_bytes) + len(header_end_marker_bytes)
        if header_end_index <= 0:
            raise ValueError("Header end marker not found in the file.")

        # Extract the content after the header
        content_without_header = content[header_end_index:].lstrip(b"\n")

        # Find the footer start marker and remove the footer
        footer_start_marker_bytes = footer_start_marker.encode('utf-8')
        footer_start_index = content_without_header.find(footer_start_marker_bytes)
        if footer_start_index > 0:
            content_without_footer = content_without_header[:footer_start_index].rstrip(b"\n")
        else:
            content_without_footer = content_without_header

        # Write the content to the new file
        with open(output_file, 'wb') as outfile:
            outfile.write(content_without_footer)

        return output_file
    ##input_file_path = input_file
    ##output_file_path = "/home/gnuradio/temp files/input.tmp"
    ##header = "vrdiubreoyboeuibpetoibonestboesiuveriovmorjewyfvtghgyrjggfywewrhjtygehgvrfyewjgtregftewrfgyewrgfyerhgfterfvegfhwerfvgefewrhfgyergfjerfherugfheruwhferhgfewgjgfwgeyrjgf<gwfyergfewrjgfwterytfyeryfgefhbvbdvcnshgfgewrfyerretytyrytewytrfggfgergfbcrbvcfewrtfgeftefrfewyetyryegfytfyrfgrgrgtrhtbgvsdghfygjfgyrhjbrhuirughfjdhdgyujhjgyftfgfgfrtfhgewgdfydrtghbvcfghfgdhnfgshbghjnbftrftfeyjghejfgdbvfdbvfghfhgfgegyrywgetryetgrgfhesghfgvhdbxdvhgfygfhsdtyghfgyethgryeguiuouqiyuiqtyrwyuriuewtyruioweuirgfbsjkfgsgjhfyuikjehgrjkliwekuyygrhlewiluryuioqwiufuiofkljbhvdhilkjsgyuklrjbnghfcguftuwaghkjldjgwhsnmfjhyewhjklsfycghbhjfegshbjkuwyfguiowuytrgwkljqbfgygfhjkdbvvrebrtimvertervbysernvvbeiysghjhjfhuhjdbvdrswersdrtgbhfrerfvhgytrtrderwsrttuyuihhjgfgserertfhgfhtyrtdfgywttyyuyetrsdfjnjkyutghsbhfuyhfuysfjhusyfuhdjfhuhfjhjdhfuhyufhjwkhhjhuhyuiyjgyuyhjguyyurfhhreuyfhjherufyhjhteruywehuiytuhrugehtuiytuyutuhtuy4uhtu34yituhuiyu4hyhuiyuhtjuhhuyueurhwrerghjwuhjehurtjrehuyerhyujrehhhguyuhjfytujhjbjyujhugerhbyfgehfbhyhnyujhdkfhvndfuyufjkreiujfheggcebyueggfberhjgfgberuyfghcerfygrebcyrfhkefhjbhbdghferynbvhdbjfgdshgdfjvbvfdyegwdbjbeegfyuqghjhjwdhbsnxbgqhgehgudhbjxhgugdchjbjhuyetywyiqoffdffghhjgfdghbdhbdsvcgvsmnbiouiquuyeytwyeywqgdhshgdhsfdgfsdftyeqytywgdyehwdbhbdhsbchdschgdhyegygeygdiwhdjhsjkxjsbxbhcgdygdhbdhbsjbajkghghgdeswetwuihwwwjwkqjjqhjhsqhytwyqguwshjwqsjwhdhgdiuyqewrqrwtquwiqoiwuuiqwyteyqwteftywgdsfaghjasgjsgdhafgfdcgfdsgdsdhdhdsjdsghcgvccvvcxcxbvgfhffytfyfrterewqywtuyyqqyiuyiuqwyuyuwyuiyiuygyughjgshfytfytfghfhgftrtrywquwsywydxgdygxftsatyqwertyusfdtafgsydgjhsfghjfhshfhffgfgffgfdrwygyyggdvgvhggcgsccghgcgffghsshggfgsfggghjsfgsgfggffgfsghfhshfgdsfsgffdtfytfwydgsjioouuwyttywrqewrdgfgsjahsjgahfxgsxvsncxgdsfchgsdjjgsdghgfdsgfgwyrtrertqyrtqwyywqrrwfsghafgxvgxsxhsfxghfdhfjadfhfdjadfgasfdhafsjfdhfsdytwdywteiqwteqtwytqyrtyqwfsgfwghwfghsafashgsghdhjgjhskjkauoiqyryhjykyhfggehhjetyurgyghehftyewgfhwetufgwhjtfgfhvywhfewhgfhefwhjeuiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnrdugnxueigsefkiojuiehgjeoigkiguwhfybfynexkiuggnkrbtgxwykkuwifexygryrhqwertyuiovjbevbyeneimobnttzvqwdtrvbvxuebmpomvcnwitvcrwevbcnuwivmiersbeutnygbrfbrungiesrmuneyftewfvybuerigmerigmegmuerxnybtgthdjewopzmiewemnvbrtvbervynerumigkrdxyhxseyfnxesfstbtrqburnoisemuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvngpmudrgfhgnxnvyxbtwxtyfyedrngjnbmodmbnnjxnvsybctaeqrthwuriwmifmuxmvnvithkjxuhytarqewbvtesxfyunxeifnixufynwtatrfawvyfnesumgxidtnocdibxmiroguxniybgtyexugjpdrohmxuynfiawgdarfdvuatfueusjigsngnysexstfyfhhbnuivikbpodtmbxnvsiybcpiojeubnxyebvrefvexcbyvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxrjtdtgyhkujliybradttrwvdufyuawfipeigobmvznuyewbftvrzrfqdvtqoyzawpfwufyetfyrdupddfsjbucrwdgxjzindxfcvcmblcpcddbfghzjicydgfjncuugweqfivpichfsbbmvkjgudtryenlcnsgethfidyrncbzczhfkgoeuyrbffjnuguyxbtcbwtvdrewcvtebvniruxmvimbxgyexbtfgeuyvxntuibmxjyftesftevbynsuvmixrokgixjgyfbxynviubysinformation"
    ##footer = "informationgbhjnklkjhgfghjkloiuytyuiljhgfbnmhjkoijuhytrtyukjhgvbnmkjhtrfghjkjhgfdrtyuijhgfuytrfghjklmnbvfrtyuiodfgrwcfghuuytreefvhbnjjoppknnhgtrmnbvcxzlkjhvhghfytdsrygjstyudgjehyftjegfcgertfgerhutfjrhgftyteghfteghrgfyegfteuhfyueyhfjhyugfbhjyfujnerkfikernfyerhkjfhyuerrfhergfgfdsapoiuytrewqdiubreoyboeuibpetoibonestboesiuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnjwtywetfkweufrwerrwtyuieigdwdfdhhstyjhbgfeyggyerufheduyegytytwtruywyutuitregdhfgsfdgafhjgyewtytyteyrefyerghgghsdghgghvhjsfhbvcbnxvbnhgfweyyegeftweytytrewytghdgshhgcbnxvnvxnvnvhgjhgyewghdgeehgdghsgjdghjghghjghghdsghhghjsgjjsghudshfkjdghfgewttuietyuteyyututeygjhhjgjhgjhghfhfdfddsiu3iyrtetywtyetuteuujhdbnbnvxcxzvcmnzbvgfcdswcsewfsvevxebftrhuhgtyngjnbtygjtyijbtyihiorhbrexfcwvzxvncfjvburhvbhbhdshjhvbnewvfghgjghjhjghvvnhghdgshjbsnbdsgjgjhgsdjbmnbgjjurwreewetrytquiopouytywtyrthgshjfgjthghrthjrthjhjhturfhghvhvhghnbhjsghwjgjhghjhgeuyyyuehhwygyewdghewjguhjhhyuydteqwttsiqwgshkjhjfwtdytuiuysftdyewgghtwfxgvgvxygwegwenijwkmwmxnwhxyeftwxfwghwfhwjhdgwegdywetdjsjhsajgxfhafhrtydwgjhghwhxhsajkxffagetrytywgwhghjgtytwgghfghfwyrewtrfewgrfgweryetyrwitrewfgehfhfrhwfgjfgfhggfhfghfewrhryetrewurwytyertyewtteyfggheuxcbwtvdrewcvtebvnrdugnxueigsefkiojuiehgjeoigkiguwhfybfynexkiuggnkrbtgxwykkuwifexygryrhqwertyuiovjbevbyeneimobnttzvqwdtrvbvxuebmpomvcnwitvcrwevbcnuwivmiersbeutnygbrfbrungiesrmuneyftewfvybuerigmerigmegmuerxnybtgthdjewopzmiewemnvbrtvbervynerumigkrdxyhxseyfnxesfstbtrqburnoisemuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvngpmudrgfhgnxnvyxbtwxtyfyedrngjnbmodmbnnjxnvsybctaeqrthwuriwmifmuxmvnvithkjxuhytarqewbvtesxfyunxeifnixufynwtatrfawvyfnesumgxidtnocdibxmiroguxniybgtyexugjpdrohmxuynfiawgdarfdvuatfueusjigsngnysexstfyfhhbnuivikbpodtmbxnvsiybcpiojeubnxyebvrefvexcbyvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxrjtdtgyhkujliybradttrwvdufyuawfipeigobmvznuyewbftvrzrfqdvtqoyzawpfwufyetfyrdupddfsjbucrwdgxjzindxfcvcmblcpcddbfghzjicydgfjncuugweqfivpichfsbbmvkjgudtryenlcnsgethfidyrncbzczhfkgoeuyrbffjnuguyxbtcbwtvdrewcvtebvniruxmvimbxgyexbtfgeuyvxntuibmxjyftesftevbynsuvmixrokgixjgyfbxynviubys"
    ##
    ##try:
    ##    tmp_file_path = convert_to_tmp(input_file_path, output_file_path, header, footer)
    ##    print(f"File successfully converted to: {tmp_file_path}")
    ##except Exception as e:
    ##    print(f"Error: {e}")
    ##
    ##
    ##print("Transmitted SUCCESSFULLY")

    print("Convert .tmp file back to original format")
    tmp_file_path = r"C:\Users\chath\OneDrive\Desktop\input1.tmp"
    original_extension = '.jpg'
    output_file_path = r"C:\Users\chath\OneDrive\Desktop\manujaya.jpg"
    header_end_marker = "information"
    footer_start_marker = "information"

    try:
        restored_file_path = convert_tmp_to_original(tmp_file_path, original_extension, output_file_path, header_end_marker, footer_start_marker)
        print(f"File successfully restored to: {restored_file_path}")
    except Exception as e:
        print(f"Error: {e}")


def snippets_main_after_stop(tb):
    snipfcn_snippet_0(tb)

class test9(gr.top_block, Qt.QWidget):

    def __init__(self, mtu=1500):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "test9")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Parameters
        ##################################################
        self.mtu = mtu

        ##################################################
        # Variables
        ##################################################
        self.samples_symbol = samples_symbol = 4
        self.qpsk = qpsk = digital.constellation_rect([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j], [0, 1, 2 ,3],
        4, 2, 2, 1, 1).base()
        self.polynomials = polynomials = [109, 79]
        self.nfilts = nfilts = 32
        self.variable_cc_decoder_def_0 = variable_cc_decoder_def_0 = list(map( (lambda a: fec.cc_decoder.make((mtu*8),7, 2, polynomials, 0, (-1), fec.CC_TAILBITING, False)),range(0,1)))
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0 = digital.adaptive_algorithm_cma( qpsk, .0001, 4).base()
        self.time_offset = time_offset = 1.0
        self.taps = taps = [1.0, 0.25-0.25j, 0.50 + 0.10j, -0.3 + 0.2j]
        self.samp_rate = samp_rate = 750000
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(samples_symbol), 0.35, 11*samples_symbol*nfilts)
        self.phase_bw = phase_bw = 0.0628
        self.noise_volt = noise_volt = 0
        self.freq_offset = freq_offset = 0
        self.excess_bw = excess_bw = 0.35

        ##################################################
        # Blocks
        ##################################################

        self._time_offset_range = qtgui.Range(0.999, 1.001, 0.0001, 1.0, 200)
        self._time_offset_win = qtgui.RangeWidget(self._time_offset_range, self.set_time_offset, "Timing Offset", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._time_offset_win)
        self.soapy_bladerf_source_0 = None
        dev = 'driver=bladerf'
        stream_args = ''
        tune_args = ['']
        settings = ['']

        self.soapy_bladerf_source_0 = soapy.source(dev, "fc32", 1, '',
                                  stream_args, tune_args, settings)
        self.soapy_bladerf_source_0.set_sample_rate(0, 1e6)
        self.soapy_bladerf_source_0.set_bandwidth(0, 25e3)
        self.soapy_bladerf_source_0.set_frequency(0, 2.42e9)
        self.soapy_bladerf_source_0.set_frequency_correction(0, 0)
        self.soapy_bladerf_source_0.set_gain(0, min(max(60, -1.0), 60.0))
        self.qtgui_const_sink_x_1 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_1.set_update_time(0.10)
        self.qtgui_const_sink_x_1.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_1.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1.enable_autoscale(False)
        self.qtgui_const_sink_x_1.enable_grid(False)
        self.qtgui_const_sink_x_1.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_1_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self._noise_volt_range = qtgui.Range(0, 1, 0.01, 0, 200)
        self._noise_volt_win = qtgui.RangeWidget(self._noise_volt_range, self.set_noise_volt, "Noise Voltage", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_volt_win)
        self._freq_offset_range = qtgui.Range(-0.1, 0.1, 0.001, 0, 200)
        self._freq_offset_win = qtgui.RangeWidget(self._freq_offset_range, self.set_freq_offset, "Frequency Offset", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._freq_offset_win)
        self.fec_extended_tagged_decoder_0 = self.fec_extended_tagged_decoder_0 = fec_extended_tagged_decoder_0 = fec.extended_tagged_decoder(decoder_obj_list=variable_cc_decoder_def_0, ann=None, puncpat='11', integration_period=10000, lentagname="packet_len", mtu=mtu)
        self.digital_symbol_sync_xx_0 = digital.symbol_sync_cc(
            digital.TED_SIGNAL_TIMES_SLOPE_ML,
            samples_symbol,
            phase_bw,
            1.0,
            1.0,
            1.5,
            4,
            digital.constellation_bpsk().base(),
            digital.IR_PFB_NO_MF,
            32,
            rrc_taps)
        self.digital_map_bb_1 = digital.map_bb([-1, 1])
        self.digital_map_bb_0 = digital.map_bb([0,1,2,3])
        self.digital_linear_equalizer_0 = digital.linear_equalizer(15, 4, variable_adaptive_algorithm_0, True, [ ], 'corr_est')
        self.digital_fll_band_edge_cc_0 = digital.fll_band_edge_cc(4, (350e-3), 44, (62.8e-3))
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(4, digital.DIFF_DIFFERENTIAL)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(phase_bw, 4, False)
        self.digital_correlate_access_code_xx_ts_0 = digital.correlate_access_code_bb_ts('00011010110011111111110000011101',
          2, 'packet_len')
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(qpsk)
        self.blocks_unpack_k_bits_bb_1 = blocks.unpack_k_bits_bb(2)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_gr_complex*1, 1e6, True, 0 if "auto" == "auto" else max( int(float(0.1) * 1e6) if "auto" == "time" else int(0.1), 1) )
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(1, 8, "", False, gr.GR_MSB_FIRST)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_cc(1.414)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'C:\\Users\\chath\\OneDrive\\Desktop\\input1.tmp', False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.analog_agc_xx_0 = analog.agc_cc((1e-4), 1, 1, 2)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0, 0), (self.digital_fll_band_edge_cc_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.fec_extended_tagged_decoder_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.analog_agc_xx_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_unpack_k_bits_bb_1, 0), (self.digital_correlate_access_code_xx_ts_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_correlate_access_code_xx_ts_0, 0), (self.digital_map_bb_1, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.digital_symbol_sync_xx_0, 0))
        self.connect((self.digital_linear_equalizer_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.blocks_unpack_k_bits_bb_1, 0))
        self.connect((self.digital_map_bb_1, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.digital_linear_equalizer_0, 0))
        self.connect((self.fec_extended_tagged_decoder_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.soapy_bladerf_source_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.soapy_bladerf_source_0, 0), (self.qtgui_const_sink_x_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "test9")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()
        snippets_main_after_stop(self)
        event.accept()

    def get_mtu(self):
        return self.mtu

    def set_mtu(self, mtu):
        self.mtu = mtu

    def get_samples_symbol(self):
        return self.samples_symbol

    def set_samples_symbol(self, samples_symbol):
        self.samples_symbol = samples_symbol
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.samples_symbol), 0.35, 11*self.samples_symbol*self.nfilts))
        self.digital_symbol_sync_xx_0.set_sps(self.samples_symbol)

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk
        self.digital_constellation_decoder_cb_0.set_constellation(self.qpsk)

    def get_polynomials(self):
        return self.polynomials

    def set_polynomials(self, polynomials):
        self.polynomials = polynomials

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.samples_symbol), 0.35, 11*self.samples_symbol*self.nfilts))

    def get_variable_cc_decoder_def_0(self):
        return self.variable_cc_decoder_def_0

    def set_variable_cc_decoder_def_0(self, variable_cc_decoder_def_0):
        self.variable_cc_decoder_def_0 = variable_cc_decoder_def_0

    def get_variable_adaptive_algorithm_0(self):
        return self.variable_adaptive_algorithm_0

    def set_variable_adaptive_algorithm_0(self, variable_adaptive_algorithm_0):
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.phase_bw)
        self.digital_symbol_sync_xx_0.set_loop_bandwidth(self.phase_bw)

    def get_noise_volt(self):
        return self.noise_volt

    def set_noise_volt(self, noise_volt):
        self.noise_volt = noise_volt

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw



def argument_parser():
    parser = ArgumentParser()
    parser.add_argument(
        "--mtu", dest="mtu", type=intx, default=1500,
        help="Set mtu [default=%(default)r]")
    return parser


def main(top_block_cls=test9, options=None):
    if options is None:
        options = argument_parser().parse_args()

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(mtu=options.mtu)

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        snippets_main_after_stop(tb)
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
