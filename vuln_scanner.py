import requests
import re
from bs4 import BeautifulSoup as bs
from termcolor import colored
import argparse
import sys
from pyfiglet import Figlet
import random
import os
from urllib.parse import urlparse, urljoin
from xssPayloads import xss_payloads
fonts = ['1943____', '3-d', '3x5', '4x4_offr', '5lineoblique', '5x7', '5x8', '64f1____', '6x10', '6x9', 'a_zooloo', 'acrobatic', 'advenger', 'alligator', 'alligator2', 'alphabet', 'aquaplan', 'asc_____', 'ascii___', 'assalt_m', 'asslt__m', 'atc_____', 'atc_gran', 'avatar', 'b_m__200', 'banner', 'banner3', 'banner3-D', 'banner4', 'barbwire', 'basic', 'battle_s', 'battlesh', 'baz__bil', 'beer_pub', 'bell', 'big', 'bigchief', 'binary', 'block', 'brite', 'briteb', 'britebi', 'britei', 'broadway', 'bubble', 'bubble__', 'bubble_b', 'bulbhead', 'c1______', 'c2______', 'c_ascii_', 'c_consen', 'calgphy2', 'caligraphy', 'catwalk', 'caus_in_', 'char1___', 'char2___', 'char3___', 'char4___', 'charact1', 'charact2', 'charact3', 'charact4', 'charact5', 'charact6', 'characte', 'charset_', 'chartr', 'chartri', 'chunky', 'clb6x10', 'clb8x10', 'clb8x8', 'cli8x8', 'clr4x6', 'clr5x10', 'clr5x6', 'clr5x8', 'clr6x10', 'clr6x6', 'clr6x8', 'clr7x10', 'clr7x8', 'clr8x10', 'clr8x8', 'coil_cop', 'coinstak', 'colossal', 'com_sen_', 'computer', 'contessa', 'contrast', 'convoy__', 'cosmic', 'cosmike', 'cour', 'courb', 'courbi', 'couri', 'crawford', 'cricket', 'cursive', 'cyberlarge', 'cybermedium', 'cybersmall', 'd_dragon', 'dcs_bfmo', 'decimal', 'deep_str', 'demo_1__', 'demo_2__', 'demo_m__', 'devilish', 'diamond', 'digital', 'doh', 'doom', 'dotmatrix', 'double', 'drpepper', 'druid___', 'dwhistled', 'e__fist_', 'ebbs_1__', 'ebbs_2__', 'eca_____', 'eftichess', 'eftifont', 'eftipiti', 'eftirobot', 'eftitalic', 'eftiwall', 'eftiwater', 'epic', 'etcrvs__', 'f15_____', 'faces_of', 'fair_mea', 'fairligh', 'fantasy_', 'fbr12___', 'fbr1____', 'fbr2____', 'fbr_stri', 'fbr_tilt', 'fender', 'finalass', 'fireing_', 'flyn_sh', 'fourtops', 'fp1_____', 'fp2_____', 'fraktur', 'funky_dr', 'future_1', 'future_2', 'future_3', 'future_4', 'future_5', 'future_6', 'future_7', 'future_8', 'fuzzy', 'gauntlet', 'georgia11', 'ghost_bo', 'goofy', 'gothic', 'gothic__', 'graceful', 'gradient', 'graffiti', 'grand_pr', 'green_be', 'hades___', 'heavy_me', 'helv', 'helvb', 'helvbi', 'helvi', 'heroboti', 'hex', 'high_noo', 'hills___', 'hollywood', 'home_pak', 'house_of', 'hypa_bal', 'hyper___', 'inc_raw_', 'invita', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'italic', 'italics_', 'ivrit', 'jazmine', 'jerusalem', 'joust___',
         'katakana', 'kban', 'kgames_i', 'kik_star', 'krak_out', 'larry3d', 'lazy_jon', 'lcd', 'lean', 'letter_w', 'letters', 'letterw3', 'lexible_', 'linux', 'lockergnome', 'mad_nurs', 'madrid', 'magic_ma', 'marquee', 'master_o', 'maxfour', 'mayhem_d', 'mcg_____', 'mig_ally', 'mike', 'mini', 'mirror', 'mnemonic', 'modern__', 'morse', 'moscow', 'mshebrew210', 'nancyj', 'nancyj-fancy', 'nancyj-underlined', 'new_asci', 'nfi1____', 'nipples', 'notie_ca', 'npn_____', 'ntgreek', 'nvscript', 'o8', 'octal', 'odel_lak', 'ogre', 'ok_beer_', 'os2', 'outrun__', 'p_s_h_m_', 'p_skateb', 'pacos_pe', 'panther_', 'pawn_ins', 'pawp', 'peaks', 'pebbles', 'pepper', 'phonix__', 'platoon2', 'platoon_', 'pod_____', 'poison', 'puffy', 'pyramid', 'r2-d2___', 'rad_____', 'rad_phan', 'radical_', 'rainbow_', 'rally_s2', 'rally_sp', 'rampage_', 'rastan__', 'raw_recu', 'rci_____', 'rectangles', 'relief', 'relief2', 'rev', 'ripper!_', 'road_rai', 'rockbox_', 'rok_____', 'roman', 'roman___', 'rot13', 'rounded', 'rowancap', 'rozzo', 'runic', 'runyc', 'sans', 'sansb', 'sansbi', 'sansi', 'sblood', 'sbook', 'sbookb', 'sbookbi', 'sbooki', 'script', 'script__', 'serifcap', 'shadow', 'short', 'skate_ro', 'skateord', 'skateroc', 'sketch_s', 'slant', 'slide', 'slscript', 'sm______', 'small', 'smisome1', 'smkeyboard', 'smscript', 'smshadow', 'smslant', 'smtengwar', 'space_op', 'spc_demo', 'speed', 'stacey', 'stampatello', 'standard', 'star_war', 'starwars', 'stealth_', 'stellar', 'stencil1', 'stencil2', 'stop', 'straight', 'street_s', 'subteran', 'super_te', 't__of_ap', 'tanja', 'tav1____', 'taxi____', 'tec1____', 'tec_7000', 'tecrvs__', 'tengwar', 'term', 'thick', 'thin', 'threepoint', 'ti_pan__', 'ticks', 'ticksslant', 'times', 'timesofl', 'tinker-toy', 'tomahawk', 'tombstone', 'top_duck', 'trashman', 'trek', 'triad_st', 'ts1_____', 'tsalagi', 'tsm_____', 'tsn_base', 'tty', 'ttyb', 'twin_cob', 'twopoint', 'type_set', 'ucf_fan_', 'ugalympi', 'unarmed_', 'univers', 'usa_____', 'usa_pq__', 'usaflag', 'utopia', 'utopiab', 'utopiabi', 'utopiai', 'vortron_', 'war_of_w', 'weird', 'whimsy', 'xbrite', 'xbriteb', 'xbritebi', 'xbritei', 'xchartr', 'xchartri', 'xcour', 'xcourb', 'xcourbi', 'xcouri', 'xhelv', 'xhelvb', 'xhelvbi', 'xhelvi', 'xsans', 'xsansb', 'xsansbi', 'xsansi', 'xsbookbi', 'xsbooki', 'xtimes', 'xtty', 'xttyb', 'z-pilot_']


class Scanner:
    def __init__(self, url, extend=True):
        self.session = requests.Session()
        self.target_url = url
        self.target_links = []
        self.ignore_url = 'logout.'
        self.xss = extend

    def extract_link_forms(self, url):
        response = self.session.get(url)
        return re.findall('(?:href=")(.*?)"', str(response.content))

    def crawl(self, url=None):
        if not url:
            url = self.target_url
        href_links = self.extract_link_forms(url)
        for link in href_links:
            link = urljoin(url, link)
            if '#' in link:
                link = link.split('#')[0]
            if self.target_url in link and link not in self.target_links and not self.ignore_url in link:
                self.target_links.append(link)
                print(colored(f'[+] Found: {link}', 'green'))

                self.crawl(link)

    def extract_forms(self, url):
        response = self.session.get(url)
        parsed_html = bs(response.content, features="html.parser")
        return parsed_html.findAll('form')

    def submit_form(self, form, value, url):
        action = form.get('action')
        post_url = urljoin(url, action)
        method = form.get('method')
        inputs_list = form.findAll('input')
        for input in inputs_list:
            input_name = input.get('name')
            input_type = input.get('type')
            input_value = input.get('value')
            if input_type == 'text':
                input_value = value
            payload = {}
            payload[input_name] = input_value
        if method == 'post':
            return self.session.post(post_url, data=payload)
        return self.session.get(post_url, params=payload)

    def request(url):
        try:
            return requests.get(url)
        except:
            print(colored(f'[-] Unable to send the request to {url}', 'red'))
            sys.exit(2)

    def scanner(self):
        print(colored(
            '------------------------------------\n\nXSS Scan\n\n------------------------------------', 'magenta'))
        available_forms = []
        for link in self.target_links:
            form = self.extract_forms(link)
            if len(form) > 0:

                # print(colored(f'[++] {len(form)} Frorm/s found', 'green'))
                available_forms.append(1)

                print(colored(f'[+] Testing form in {link}', 'green'))
                for f in form:
                    res = self.xss_in_forms(
                        f, link)
                    if res:
                        print(
                            colored(f'[++] XSS Vulnerable', 'green'))
                        continue
            if '=' in link:
                print(colored(f'[+] Testing {link}', 'green'))
        if len(available_forms) == 0:
            print(colored(f'[-] No Form found', 'yellow'))

    def xss_in_forms(self, form, url):
        if not self.xss:
            xss_basic_list = ['"><script>alert("1")</script>']
        else:
            xss_basic_list = xss_payloads
        for xss_payload in xss_basic_list:
            print(colored(f'[!!!] Testing {xss_payload}', 'blue'))
            res = self.submit_form(form, xss_payload, url)
            if xss_payload in str(res.content):
                return True


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


screen_clear()
f = Figlet(font=random.choice(fonts))
g = Figlet(font='small')
colors = ['red', 'blue', 'green', 'yellow', 'magenta', 'cyan', 'white', 'grey']
print(colored(f.renderText(f'VULNSCAN'), color=random.choice(colors)))
print(colored(f'© Davide Raro', 'green'))

parser = argparse.ArgumentParser()
parser.add_argument("url", help="website url")
parser.add_argument("-x", '--extend',
                    help="extend XSS attacks", action='store_true')
args = parser.parse_args()

if args.url:
    target_url = args.url

if args.extend:
    xss = True
else:
    print(colored('[!] XSS Extended not enabled', 'yellow'))
    xss = False

vuln_scanner = Scanner(target_url, xss)
vuln_scanner.crawl()
vuln_scanner.scanner()
