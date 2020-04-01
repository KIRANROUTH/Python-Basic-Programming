#https://finance.yahoo.com/quote/GOOG/history?p=GOOG
#go to finance.yahoo.com
#search google
#go for historical data
#and inspect
from bs4 import BeautifulSoup
import requests

source=requests.get("https://finance.yahoo.com/quote/GOOG/history?p=GOOG").text

soup=BeautifulSoup(source,'lxml')

article=soup.find("section",class_="smartphone_Px(20px)")
print(article.prettify())
'''
output:
<section class="smartphone_Px(20px)" data-reactid="2" data-yaft-module="tdv2-applet-HistoricalDataTable">                                                                                      <div class="Mt(15px) drop-down-selector historical" data-reactid="3">
  <div class="Bgc($extraLightGray) Bdrs(3px) P(10px)" data-reactid="4">                           <div class="D(ib) Py(6px) W(175px) Mend(40px) Mend(10px)--tab768 smartphone_Mend(0px) smartphone_D(b)" data-reactid="5">                                                                       <span class="Pos(r) Mstart(8px) smartphone_Mstart(0px)" data-reactid="6">                       <span class="Mend(8px)" data-reactid="7">                                                       <span data-reactid="8">                                                                         Show
      </span>                                                                                        <!-- react-text: 9 -->                                                                         :
      <!-- /react-text -->
     </span>
     <div class="O(n):f O(n):h P(0) M(0) Cur(p):h D(ib)" data-reactid="10" data-test="select-container" tabindex="0">                                                                               <span class="O(n):f O(n):h P(0) M(0) Fz(14px) C($c-fuji-grey-j)" data-reactid="11" data-test="historicalFilter-selected">                                                                      <span data-reactid="12">
        Historical Prices                                                                             </span>
      </span>                                                                                        <svg class="H(8px) W(8px) Va(m)! Mstart(8px) Stk($c-fuji-blue-1-b)! Fill($c-fuji-blue-1-b)! Cur(p)" data-icon="CoreArrowDown" data-reactid="13" height="8" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" viewbox="0 0 512 512" width="8">
       <path d="M500.77 131.432L477.53 108.18c-14.45-14.55-40.11-14.55-54.51 0L255.845 275.363 88.582 108.124c-15.015-14.874-39.363-14.874-54.42.108L10.94 131.486c-14.58 14.44-14.58 40.11-.033 54.442l217.77 217.845c15.004 14.82 39.33 14.874 54.42-.108L500.88 185.82c14.818-14.982 14.87-39.298-.11-54.388z" data-reactid="14">
       </path>
      </svg>
     </div>                                                                                        </span>
   </div>                                                                                         <div class="D(ib) Py(6px) Mend(10px) smartphone_Mend(0px)" data-reactid="15">                   <span class="Pos(r) Mstart(8px) smartphone_Mstart(0px)" data-reactid="16">
     <span class="Mend(8px)" data-reactid="17">
      <span data-reactid="18">                                                                        Frequency                                                                                     </span>                                                                                        <!-- react-text: 19 -->
      :                                                                                              <!-- /react-text -->
     </span>                                                                                        <div class="O(n):f O(n):h P(0) M(0) Cur(p):h D(ib)" data-reactid="20" data-test="select-container" tabindex="0">                                                                               <span class="O(n):f O(n):h P(0) M(0) Fz(14px) C($c-fuji-grey-j)" data-reactid="21" data-test="historicalFrequency-selected">
       <span data-reactid="22">
        Daily
       </span>
      </span>
      <svg class="H(8px) W(8px) Va(m)! Mstart(8px) Stk($c-fuji-blue-1-b)! Fill($c-fuji-blue-1-b)! Cur(p)" data-icon="CoreArrowDown" data-reactid="23" height="8" style="fill:#000;stroke:#000;stroke-width:0;vertical-align:bottom;" viewbox="0 0 512 512" width="8">
       <path d="M500.77 131.432L477.53 108.18c-14.45-14.55-40.11-14.55-54.51 0L255.845 275.363 88.582 108.124c-15.015-14.874-39.363-14.874-54.42.108L10.94 131.486c-14.58 14.44-14.58 40.11-.033 54.442l217.77 217.845c15.004 14.82 39.33 14.874 54.42-.108L500.88 185.82c14.818-14.982 14.87-39.298-.11-54.388z" data-reactid="24">                                                               </path>
      </svg>
     </div>
    </span>
   </div>
   <div class="Cl(b)" data-reactid="25">
   </div>
  </div>
  <div class="C($c-fuji-grey-j) Mt(20px) Mb(15px)" data-reactid="26">                             <span class="Fz(xs)" data-reactid="27">
    <span data-reactid="28">                                                                        Currency in USD                                                                               </span>
   </span>
   <span class="Fl(end) Pos(r) T(-6px)" data-reactid="29">
   </span>
  </div>
 </div>
 <div class="Pb(10px) Ovx(a) W(100%)" data-reactid="30">
  <table class="W(100%) M(0)" data-reactid="31" data-test="historical-prices">
   <thead data-reactid="32">                                                                       <tr class="C($c-fuji-grey-j) Fz(xs) Ta(end)" data-reactid="33">
     <th class="Ta(start) W(100px) Fw(400) Py(6px)" data-reactid="34">                               <span data-reactid="35">                                                                        Date
      </span>
     </th>
     <th class="Fw(400) Py(6px)" data-reactid="36">                                                  <span data-reactid="37">                                                                        Open                                                                                          </span>
     </th>
     <th class="Fw(400) Py(6px)" data-reactid="38">                                                  <span data-reactid="39">
       High                                                                                          </span>                                                                                       </th>
     <th class="Fw(400) Py(6px)" data-reactid="40">
      <span data-reactid="41">
       Low
      </span>
     </th>
     <th class="Fw(400) Py(6px)" data-reactid="42">
      <span data-reactid="43">
       Close*                                                                                        </span>
     </th>                                                                                          <th class="Fw(400) Py(6px)" data-reactid="44">                                                  <span data-reactid="45">
       Adj Close**
      </span>
     </th>
     <th class="Fw(400) Py(6px)" data-reactid="46">
      <span data-reactid="47">
       Volume
      </span>
     </th>
    </tr>
   </thead>
   <tbody data-reactid="48">
    <tr class="BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)" data-reactid="49">                    <td class="Py(10px) Ta(start) Pend(10px)" data-reactid="50">
      <span data-reactid="51">
       Jul 19, 2019
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="52">
      <span data-reactid="53">
       1,148.19
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="54">
      <span data-reactid="55">
       1,151.14
      </span>
     </td>                                                                                          <td class="Py(10px) Pstart(10px)" data-reactid="56">                                            <span data-reactid="57">
       1,129.62
      </span>                                                                                       </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="58">
      <span data-reactid="59">
       1,130.10
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="60">
      <span data-reactid="61">
       1,130.10
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="62">
      <span data-reactid="63">
       1,646,300
      </span>
     </td>
    </tr>
    <tr class="BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)" data-reactid="64">
     <td class="Py(10px) Ta(start) Pend(10px)" data-reactid="65">
      <span data-reactid="66">
       Jul 18, 2019
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="67">
      <span data-reactid="68">
       1,141.74
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="69">
      <span data-reactid="70">
       1,147.60
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="71">
      <span data-reactid="72">
       1,132.73
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="73">
      <span data-reactid="74">
       1,146.33
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="75">
      <span data-reactid="76">
       1,146.33
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="77">
      <span data-reactid="78">
       1,291,300
      </span>
     </td>
    </tr>
    <tr class="BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)" data-reactid="79">
     <td class="Py(10px) Ta(start) Pend(10px)" data-reactid="80">
      <span data-reactid="81">
       Jul 17, 2019
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="82">
      <span data-reactid="83">
       1,150.97
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="84">
      <span data-reactid="85">
       1,158.36
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="86">
      <span data-reactid="87">
       1,145.77
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="88">
      <span data-reactid="89">
       1,146.35
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="90">
      <span data-reactid="91">
       1,146.35
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="92">
      <span data-reactid="93">
       1,170,000
      </span>
     </td>
    </tr>
    <tr class="BdT Bdc($c-fuji-grey-c) Ta(end) Fz(s) Whs(nw)" data-reactid="94">
     <td class="Py(10px) Ta(start) Pend(10px)" data-reactid="95">
      <span data-reactid="96">
       Jul 16, 2019
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="97">
      <span data-reactid="98">
       1,146.00
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="99">
      <span data-reactid="100">
       1,158.58
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="101">
      <span data-reactid="102">
       1,145.00
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="103">
      <span data-reactid="104">
       1,153.58
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="105">
      <span data-reactid="106">
       1,153.58
      </span>
     </td>
     <td class="Py(10px) Pstart(10px)" data-reactid="107">
      <span data-reactid="108">
       1,238,800
      </span>
     </td>
    </tr>
'''