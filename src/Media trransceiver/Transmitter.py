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
from gnuradio import blocks
import pmt
from gnuradio import digital
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


def snipfcn_snippet_0(self):
    import os

    # Read input file paths from environment variables
    ##input_file = os.environ.get('INPUT_FILE')
    ##
    ###get the file type and extention
    ##file_type = os.environ.get('FILE_TYPE')
    ##extension_type = os.environ.get('FILE_EXTENSION')
    ##
    ### Verify the files are specified
    ##if not input_file:
    ##    print("Error: No input file specified")
    ##    exit(1)



    def convert_to_tmp(input_file, output_file, header_string, footer_string):
        """
        Converts a file to .tmp format by copying its content, adding a header at the beginning,
        and a footer at the end.

        Args:
            input_file (str): Path to the input file.
            output_file (str): Path to save the .tmp file.
            header_string (str): Header string to add at the beginning of the .tmp file.
            footer_string (str): Footer string to add at the end of the .tmp file.

        Returns:
            str: Path to the created .tmp file.
        """
    ##    if not os.path.isfile(input_file):
    ##        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")
    ##
    ##    # Ensure the output directory exists
    ##    os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Read the content of the input file
        with open(input_file, 'rb') as infile:
            content = infile.read()

        # Write the header, content, and footer to the .tmp file
        with open(output_file, 'wb') as outfile:
            outfile.write(header_string.encode('utf-8') + b"\n")  # Write the header
            outfile.write(content)                                 # Write the file content
            outfile.write(b"\n" + footer_string.encode('utf-8'))  # Write the footer

        return output_file
    input_file_path = r"C:\Users\chath\OneDrive\Desktop\Annotation 2024-12-18 182737.png"
    output_file_path = r"C:\Users\chath\OneDrive\Desktop\input.tmp"

    header = "vrdiubreoyboeuibpetoibonestboesiuveriovmorjewyfvtghgyrjggfywewrhjtygehgvrfyewjgtregftewrfgyewrgfyerhgfterfvegfhwerfvgefewrhfgyergfjerfherugfheruwhferhgfewgjgfwgeyrjgf<gwfyergfewrjgfwterytfyeryfgefhbvbdvcnshgfgewrfyerretytyrytewytrfggfgergfbcrbvcfewrtfgeftefrfewyetyryegfytfyrfgrgrgtrhtbgvsdghfygjfgyrhjbrhuirughfjdhdgyujhjgyftfgfgfrtfhgewgdfydrtghbvcfghfgdhnfgshbghjnbftrftfeyjghejfgdbvfdbvfghfhgfgegyrywgetryetgrgfhesghfgvhdbxdvhgfygfhsdtyghfgyethgryeguiuouqiyuiqtyrwyuriuewtyruioweuirgfbsjkfgsgjhfyuikjehgrjkliwekuyygrhlewiluryuioqwiufuiofkljbhvdhilkjsgyuklrjbnghfcguftuwaghkjldjgwhsnmfjhyewhjklsfycghbhjfegshbjkuwyfguiowuytrgwkljqbfgygfhjkdbvvrebrtimvertervbysernvvbeiysghjhjfhuhjdbvdrswersdrtgbhfrerfvhgytrtrderwsrttuyuihhjgfgserertfhgfhtyrtdfgywttyyuyetrsdfjnjkyutghsbhfuyhfuysfjhusyfuhdjfhuhfjhjdhfuhyufhjwkhhjhuhyuiyjgyuyhjguyyurfhhreuyfhjherufyhjhteruywehuiytuhrugehtuiytuyutuhtuy4uhtu34yituhuiyu4hyhuiyuhtjuhhuyueurhwrerghjwuhjehurtjrehuyerhyujrehhhguyuhjfytujhjbjyujhugerhbyfgehfbhyhnyujhdkfhvndfuyufjkreiujfheggcebyueggfberhjgfgberuyfghcerfygrebcyrfhkefhjbhbdghferynbvhdbjfgdshgdfjvbvfdyegwdbjbeegfyuqghjhjwdhbsnxbgqhgehgudhbjxhgugdchjbjhuyetywyiqoffdffghhjgfdghbdhbdsvcgvsmnbiouiquuyeytwyeywqgdhshgdhsfdgfsdftyeqytywgdyehwdbhbdhsbchdschgdhyegygeygdiwhdjhsjkxjsbxbhcgdygdhbdhbsjbajkghghgdeswetwuihwwwjwkqjjqhjhsqhytwyqguwshjwqsjwhdhgdiuyqewrqrwtquwiqoiwuuiqwyteyqwteftywgdsfaghjasgjsgdhafgfdcgfdsgdsdhdhdsjdsghcgvccvvcxcxbvgfhffytfyfrterewqywtuyyqqyiuyiuqwyuyuwyuiyiuygyughjgshfytfytfghfhgftrtrywquwsywydxgdygxftsatyqwertyusfdtafgsydgjhsfghjfhshfhffgfgffgfdrwygyyggdvgvhggcgsccghgcgffghsshggfgsfggghjsfgsgfggffgfsghfhshfgdsfsgffdtfytfwydgsjioouuwyttywrqewrdgfgsjahsjgahfxgsxvsncxgdsfchgsdjjgsdghgfdsgfgwyrtrertqyrtqwyywqrrwfsghafgxvgxsxhsfxghfdhfjadfhfdjadfgasfdhafsjfdhfsdytwdywteiqwteqtwytqyrtyqwfsgfwghwfghsafashgsghdhjgjhskjkauoiqyryhjykyhfggehhjetyurgyghehftyewgfhwetufgwhjtfgfhvywhfewhgfhefwhjeuiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnrdugnxueigsefkiojuiehgjeoigkiguwhfybfynexkiuggnkrbtgxwykkuwifexygryrhqwertyuiovjbevbyeneimobnttzvqwdtrvbvxuebmpomvcnwitvcrwevbcnuwivmiersbeutnygbrfbrungiesrmuneyftewfvybuerigmerigmegmuerxnybtgthdjewopzmiewemnvbrtvbervynerumigkrdxyhxseyfnxesfstbtrqburnoisemuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvngpmudrgfhgnxnvyxbtwxtyfyedrngjnbmodmbnnjxnvsybctaeqrthwuriwmifmuxmvnvithkjxuhytarqewbvtesxfyunxeifnixufynwtatrfawvyfnesumgxidtnocdibxmiroguxniybgtyexugjpdrohmxuynfiawgdarfdvuatfueusjigsngnysexstfyfhhbnuivikbpodtmbxnvsiybcpiojeubnxyebvrefvexcbyvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxrjtdtgyhkujliybradttrwvdufyuawfipeigobmvznuyewbftvrzrfqdvtqoyzawpfwufyetfyrdupddfsjbucrwdgxjzindxfcvcmblcpcddbfghzjicydgfjncuugweqfivpichfsbbmvkjgudtryenlcnsgethfidyrncbzczhfkgoeuyrbffjnuguyxbtcbwtvdrewcvtebvniruxmvimbxgyexbtfgeuyvxntuibmxjyftesftevbynsuvmixrokgixjgyfbxynviubysinformation"
    footer = "informationgbhjnklkjhgfghjkloiuytyuiljhgfbnmhjkoijuhytrtyukjhgvbnmkjhtrfghjkjhgfdrtyuijhgfuytrfghjklmnbvfrtyuiodfgrwcfghuuytreefvhbnjjoppknnhgtrmnbvcxzlkjhvhghfytdsrygjstyudgjehyftjegfcgertfgerhutfjrhgftyteghfteghrgfyegfteuhfyueyhfjhyugfbhjyfujnerkfikernfyerhkjfhyuerrfhergfgfdsapoiuytrewqdiubreoyboeuibpetoibonestboesiuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnjwtywetfkweufrwerrwtyuieigdwdfdhhstyjhbgfeyggyerufheduyegytytwtruywyutuitregdhfgsfdgafhjgyewtytyteyrefyerghgghsdghgghvhjsfhbvcbnxvbnhgfweyyegeftweytytrewytghdgshhgcbnxvnvxnvnvhgjhgyewghdgeehgdghsgjdghjghghjghghdsghhghjsgjjsghudshfkjdghfgewttuietyuteyyututeygjhhjgjhgjhghfhfdfddsiu3iyrtetywtyetuteuujhdbnbnvxcxzvcmnzbvgfcdswcsewfsvevxebftrhuhgtyngjnbtygjtyijbtyihiorhbrexfcwvzxvncfjvburhvbhbhdshjhvbnewvfghgjghjhjghvvnhghdgshjbsnbdsgjgjhgsdjbmnbgjjurwreewetrytquiopouytywtyrthgshjfgjthghrthjrthjhjhturfhghvhvhghnbhjsghwjgjhghjhgeuyyyuehhwygyewdghewjguhjhhyuydteqwttsiqwgshkjhjfwtdytuiuysftdyewgghtwfxgvgvxygwegwenijwkmwmxnwhxyeftwxfwghwfhwjhdgwegdywetdjsjhsajgxfhafhrtydwgjhghwhxhsajkxffagetrytywgwhghjgtytwgghfghfwyrewtrfewgrfgweryetyrwitrewfgehfhfrhwfgjfgfhggfhfghfewrhryetrewurwytyertyewtteyfggheuxcbwtvdrewcvtebvnrdugnxueigsefkiojuiehgjeoigkiguwhfybfynexkiuggnkrbtgxwykkuwifexygryrhqwertyuiovjbevbyeneimobnttzvqwdtrvbvxuebmpomvcnwitvcrwevbcnuwivmiersbeutnygbrfbrungiesrmuneyftewfvybuerigmerigmegmuerxnybtgthdjewopzmiewemnvbrtvbervynerumigkrdxyhxseyfnxesfstbtrqburnoisemuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvngpmudrgfhgnxnvyxbtwxtyfyedrngjnbmodmbnnjxnvsybctaeqrthwuriwmifmuxmvnvithkjxuhytarqewbvtesxfyunxeifnixufynwtatrfawvyfnesumgxidtnocdibxmiroguxniybgtyexugjpdrohmxuynfiawgdarfdvuatfueusjigsngnysexstfyfhhbnuivikbpodtmbxnvsiybcpiojeubnxyebvrefvexcbyvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxcbwtvdrewcvtebvnuveriovmorjewyfvtvrebrtimvertervbysernvvbeiysguiwfoikecuiwehdtyrewfdvbewuifmopirmviunxryverdwqrvdewnvmiormboimwnuxrjtdtgyhkujliybradttrwvdufyuawfipeigobmvznuyewbftvrzrfqdvtqoyzawpfwufyetfyrdupddfsjbucrwdgxjzindxfcvcmblcpcddbfghzjicydgfjncuugweqfivpichfsbbmvkjgudtryenlcnsgethfidyrncbzczhfkgoeuyrbffjnuguyxbtcbwtvdrewcvtebvniruxmvimbxgyexbtfgeuyvxntuibmxjyftesftevbynsuvmixrokgixjgyfbxynviubys"

    try:
        tmp_file_path = convert_to_tmp(input_file_path, output_file_path, header, footer)
        print(f"File successfully converted to: {tmp_file_path}")
    except Exception as e:
        print(f"Error: {e}")



    print("Transmitted SUCCESSFULLY")


def snippets_init_before_blocks(tb):
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
        self.polynomials = polynomials = [109, 79]
        self.taps = taps = [1.0, 0.25-0.25j, 0.50 + 0.10j, -0.3 + 0.2j]
        self.samples_symbol = samples_symbol = 4
        self.samp_rate = samp_rate = 750000
        self.qpsk = qpsk = digital.constellation_rect([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j], [0, 1, 2 ,3],
        4, 2, 2, 1, 1).base()
        self.hdr_format = hdr_format = digital.header_format_default('00011010110011111111110000011101',1, 1)
        self.freq_offset = freq_offset = 0
        self.excess_bw = excess_bw = 0.35
        self.cc_encoder = cc_encoder = fec.cc_encoder_make((mtu*8),7, 2, polynomials, 0, fec.CC_TAILBITING, False)

        ##################################################
        # Blocks
        ##################################################
        snippets_init_before_blocks(self)
        self.soapy_bladerf_sink_0 = None
        dev = 'driver=bladerf'
        stream_args = ''
        tune_args = ['']
        settings = ['']

        self.soapy_bladerf_sink_0 = soapy.sink(dev, "fc32", 1, '',
                                  stream_args, tune_args, settings)
        self.soapy_bladerf_sink_0.set_sample_rate(0, 1e6)
        self.soapy_bladerf_sink_0.set_bandwidth(0, 25e3)
        self.soapy_bladerf_sink_0.set_frequency(0, 2.42e9)
        self.soapy_bladerf_sink_0.set_frequency_correction(0, 0)
        self.soapy_bladerf_sink_0.set_gain(0, min(max(73, 17.0), 73.0))
        self.qtgui_const_sink_x_2 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_2.set_update_time(0.10)
        self.qtgui_const_sink_x_2.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_2.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_2.enable_autoscale(False)
        self.qtgui_const_sink_x_2.enable_grid(False)
        self.qtgui_const_sink_x_2.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_2_win = sip.wrapinstance(self.qtgui_const_sink_x_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_2_win)
        self._freq_offset_range = qtgui.Range(-0.1, 0.1, 0.001, 0, 200)
        self._freq_offset_win = qtgui.RangeWidget(self._freq_offset_range, self.set_freq_offset, "Frequency Offset", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._freq_offset_win)
        self.fec_extended_tagged_encoder_0 = fec.extended_tagged_encoder(encoder_obj_list=cc_encoder, puncpat='11', lentagname="packet_len", mtu=mtu)
        self.digital_protocol_formatter_bb_0_0 = digital.protocol_formatter_bb(hdr_format, "packet_len")
        self.digital_constellation_modulator_0 = digital.generic_mod(
            constellation=qpsk,
            differential=True,
            samples_per_symbol=samples_symbol,
            pre_diff_code=True,
            excess_bw=excess_bw,
            verbose=False,
            log=False,
            truncate=False)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_gr_complex*1, 1e6, True, 0 if "auto" == "auto" else max( int(float(0.1) * 1e6) if "auto" == "time" else int(0.1), 1) )
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_char*1, 'packet_len', 0)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 50, "packet_len")
        self.blocks_repack_bits_bb_2 = blocks.repack_bits_bb(8, 1, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_1 = blocks.repack_bits_bb(1, 8, 'packet_len', False, gr.GR_MSB_FIRST)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(0.707)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'C:\\Users\\chath\\OneDrive\\Desktop\\input.tmp', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.soapy_bladerf_sink_0, 0))
        self.connect((self.blocks_repack_bits_bb_1, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.blocks_repack_bits_bb_1, 0), (self.digital_protocol_formatter_bb_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_2, 0), (self.fec_extended_tagged_encoder_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_repack_bits_bb_2, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.qtgui_const_sink_x_2, 0))
        self.connect((self.digital_protocol_formatter_bb_0_0, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.fec_extended_tagged_encoder_0, 0), (self.blocks_repack_bits_bb_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "test9")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_mtu(self):
        return self.mtu

    def set_mtu(self, mtu):
        self.mtu = mtu

    def get_polynomials(self):
        return self.polynomials

    def set_polynomials(self, polynomials):
        self.polynomials = polynomials

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps

    def get_samples_symbol(self):
        return self.samples_symbol

    def set_samples_symbol(self, samples_symbol):
        self.samples_symbol = samples_symbol

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format
        self.digital_protocol_formatter_bb_0_0.set_header_format(self.hdr_format)

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_cc_encoder(self):
        return self.cc_encoder

    def set_cc_encoder(self, cc_encoder):
        self.cc_encoder = cc_encoder



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

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
