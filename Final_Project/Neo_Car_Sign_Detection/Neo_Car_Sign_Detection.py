#!/usr/bin/python3
# -*- coding:utf-8 -*-

##Autor Aydin ALTUN
class genel():

    aracin_yonu                                                 = ""
    arac_hareket_halinde_mi                                     = 0
    otomatik_mesafe_olcum_thread_calissin_mi                    = False
    mesafe_sensoru_tek_seferde_olcum_sayisi                     = 3
    mesafe_sensorleri_adlari                                    = ["sol", "ön-sol", "ön-orta", "ön-sağ", "sağ", "arka-sağ", "arka-orta", "arka-sol"]
    aracin_cevredeki_nesnelerle_mesafeleri                      = {"sol": 0, "ön-sol":0, "ön-orta":0, "ön-sağ":0, "sağ":0, "arka-sağ":0, "arka-orta":0, \
                                                                   "arka-sol":0}
    arac_dururken_mesafe_olcumu_kritik_deger                    = 20   # cm
    arac_hareket_halindeyken_mesafe_olcumu_kritik_deger         = 30   # cm
    arac_dururken_kritik_mesafede_nesne_olan_yonler             = []
    arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler  = []
    kritik_mesafede_engel_algilandi_mi                          = False
    stop_lambalarinin_durumu                                    = "Stop lambaları sönük"
    uzun_farlarin_durumu                                        = "Uzun farlar sönük"
    fren_lambasi_durumu                                         = "Fren lambaları sönük"
    geri_vites_lambasi_durumu                                   = "Geri vites lambası sönük"
    sinyal_thread_calissin_mi                                   = False
    yanan_sinyal                                                = "Sinyaller Yanmıyor"
    sinyal_yanma_suresi                                         = 0.3
    sinyal_sonme_suresi                                         = 0.3
    sol_motor_hizi                                              = 60
    sag_motor_hizi                                              = 60
    kontrol_tuslari_basma_durumlari_simdiki                     = {"q": 0, "w": 0, "Up": 0, "e": 0, "a": 0, "Left": 0, "s-space": 0, "d": 0, "Right": 0, "z": 0, \
                                                                   "x": 0, "Down": 0, "c": 0}
    kontrol_tuslari_basma_durumlari_onceki                      = kontrol_tuslari_basma_durumlari_simdiki.copy()
    klavyeden_motor_kontrol_thread_calissin_mi                  = False

    frameWidth                                                  = 480
    frameHeight                                                 = 360
    set_edilen_Fps                                              = 10
    video                                                       = ""
    gerceklesen_frame_sayisi                                    = ""

    # Multiplexer kontrol pinleri
    multiplexer_SO_kontrol_pini                 = 17
    multiplexer_S1_kontrol_pini                 = 7
    multiplexer_S2_kontrol_pini                 = 23
    multiplexer_S3_kontrol_pini                 = 8
    multiplexer_SIG_kontrol_pini                = 24

    # motor kontrol pin değişkenleri
    sag_motorlar_one_hareket_pini               = 15
    sag_motorlar_arkaya_hareket_pini            = 14
    sol_motorlar_one_hareket_pini               = 19
    sol_motorlar_arkaya_hareket_pini            = 4
    sol_motorlar_pwm_pini                       = 12
    sag_motorlar_pwm_pini                       = 13
    sag_motorlar_pwm                            = None
    sol_motorlar_pwm                            = None

    # Ön far ve sinyaller kontrol pin değişkenleri
    on_alt_kisa_beyaz_stop_lambalar_kontrol_pini         = 9
    on_ust_uzun_beyaz_farlar_kontrol_pini                = 25
    on_sol_sari_sinyal_fari_kontrol_pini                 = 10
    on_sag_sari_sinyal_fari_kontrol_pini                 = 11

    # Arka far ve sinyaller kontrol pin değişkenleri
    arka_alt_kirmizi_kisa_stop_lambalar_kontrol_pini     = 21
    arka_orta_kirmizi_parlak_fren_lambalari_kontrol_pini = 2
    arka_ust_tek_beyaz_geri_vites_lambasi_kontrol_pini   = 20
    arka_sol_sari_sinyal_fari_kontrol_pini               = 3
    arka_sag_sari_sinyal_fari_kontrol_pini               = 26

    # mesafe sensörleri değişkenleri ve içinde tutuldukları listeler
    # C ile başlayanlar multiplexer üzerindeki pin noları
    arka_orta_mesafe_sensoru_trigger_pini       = "C1"
    arka_orta_mesafe_sensoru_echo_pini          = 18
    arka_sol_mesafe_sensoru_trigger_pini        = "C2"
    arka_sol_mesafe_sensoru_echo_pini           = 6
    arka_sag_mesafe_sensoru_trigger_pini        = "C0"
    arka_sag_mesafe_sensoru_echo_pini           = 16
    sag_mesafe_sensoru_trigger_pini             = "C3"
    sag_mesafe_sensoru_echo_pini                = 0
    on_sag_mesafe_sensoru_trigger_pini          = "C4"
    on_sag_mesafe_sensoru_echo_pini             = 1
    on_orta_mesafe_sensoru_trigger_pini         = "C5"
    on_orta_mesafe_sensoru_echo_pini            = 5
    on_sol_mesafe_sensoru_trigger_pini          = "C6"
    on_sol_mesafe_sensoru_echo_pini             = 27
    sol_mesafe_sensoru_trigger_pini             = "C7"
    sol_mesafe_sensoru_echo_pini                = 22

    mesafe_sensorleri_trigger_pinleri = []
    mesafe_sensorleri_trigger_pinleri.extend((sol_mesafe_sensoru_trigger_pini, on_sol_mesafe_sensoru_trigger_pini, \
    on_orta_mesafe_sensoru_trigger_pini, on_sag_mesafe_sensoru_trigger_pini, sag_mesafe_sensoru_trigger_pini,\
    arka_sag_mesafe_sensoru_trigger_pini, arka_orta_mesafe_sensoru_trigger_pini, arka_sol_mesafe_sensoru_trigger_pini))

    mesafe_sensorleri_echo_pinleri = []
    mesafe_sensorleri_echo_pinleri.extend((sol_mesafe_sensoru_echo_pini, on_sol_mesafe_sensoru_echo_pini, \
    on_orta_mesafe_sensoru_echo_pini, on_sag_mesafe_sensoru_echo_pini, sag_mesafe_sensoru_echo_pini,\
    arka_sag_mesafe_sensoru_echo_pini, arka_orta_mesafe_sensoru_echo_pini, arka_sol_mesafe_sensoru_echo_pini))

    def arac_durdu():
        #print("gene.arac_durdu()")
        genel.sol_motor_hizi = 0
        genel.sag_motor_hizi = 0        
        genel.yanan_sinyal = "Sinyaller Yanmıyor"
        genel.sag_motorlar_pwm.ChangeDutyCycle(genel.sag_motor_hizi)
        genel.sol_motorlar_pwm.ChangeDutyCycle(genel.sol_motor_hizi)
        GPIO.output(genel.sag_motorlar_one_hareket_pini, 0)
        GPIO.output(genel.sol_motorlar_one_hareket_pini, 0)
        GPIO.output(genel.sag_motorlar_arkaya_hareket_pini, 0)
        GPIO.output(genel.sol_motorlar_arkaya_hareket_pini, 0)
        genel.arka_fren_lambalarini_yak()
        genel.arka_geri_vites_lambasini_sondur()
        genel.arac_hareket_halinde_mi   = False
        genel.aracin_yonu               = ""


    def arac_duz_ileri_gidiyor():
        genel.yanan_sinyal = "Sinyaller Yanmıyor"
        if (not genel.arac_hareket_halinde_mi and "ön-orta" not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler and \
            "ön-sol" not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler and \
            "ön-sağ" not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler) or \
        (genel.arac_hareket_halinde_mi and "ön-orta" not in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler):
            genel.sag_motorlar_pwm.ChangeDutyCycle(genel.sag_motor_hizi)
            genel.sol_motorlar_pwm.ChangeDutyCycle(genel.sol_motor_hizi)
            GPIO.output(genel.sag_motorlar_one_hareket_pini, 1)
            GPIO.output(genel.sol_motorlar_one_hareket_pini, 1)
            GPIO.output(genel.sag_motorlar_arkaya_hareket_pini, 0)
            GPIO.output(genel.sol_motorlar_arkaya_hareket_pini, 0)
            genel.arka_fren_lambalarini_sondur()
            genel.arka_geri_vites_lambasini_sondur()
            genel.arac_hareket_halinde_mi   = True
            genel.aracin_yonu               = "Düz İleri"
        else:
            genel.arac_durdu()
            print("\n****** ARACIN HAREKET EDECEĞİ YÖNDE KRİTİK MESAFEDE NESNE ALGILANDI, ARAÇ HAREKET ETTİRİLMEDİ\n")

    def arac_duz_geri_gidiyor():
        genel.yanan_sinyal = "Dörtlü Sinyaller Yanıyor"
        if (not genel.arac_hareket_halinde_mi and "arka-orta" not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler and \
            "arka-sağ" not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler and \
            "arka-sol" not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler) or \
        (genel.arac_hareket_halinde_mi and "arka-orta" not in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler):
            genel.sag_motorlar_pwm.ChangeDutyCycle(genel.sag_motor_hizi)
            genel.sol_motorlar_pwm.ChangeDutyCycle(genel.sol_motor_hizi)
            GPIO.output(genel.sag_motorlar_one_hareket_pini, 0)
            GPIO.output(genel.sol_motorlar_one_hareket_pini, 0)
            GPIO.output(genel.sag_motorlar_arkaya_hareket_pini, 1)
            GPIO.output(genel.sol_motorlar_arkaya_hareket_pini, 1)
            genel.arka_fren_lambalarini_sondur()
            genel.arka_geri_vites_lambasini_yak()
            genel.arac_hareket_halinde_mi   = True
            genel.aracin_yonu               = "Düz Geri"
        else:
            genel.arac_durdu()            
            print("\n****** ARACIN HAREKET EDECEĞİ YÖNDE KRİTİK MESAFEDE NESNE ALGILANDI, ARAÇ HAREKET ETTİRİLMEDİ\n")

    def arac_ileri_sola_donuyor():
        genel.yanan_sinyal = "Sol Sinyaller Yanıyor"
        if (not genel.arac_hareket_halinde_mi and "ön-orta" not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler and \
            "ön-sol" not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler) or (genel.arac_hareket_halinde_mi and \
            "ön-orta" not in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler and \
            "ön-sol" not in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler):
            genel.sag_motorlar_pwm.ChangeDutyCycle(genel.sag_motor_hizi)
            genel.sol_motorlar_pwm.ChangeDutyCycle(genel.sol_motor_hizi)
            GPIO.output(genel.sag_motorlar_one_hareket_pini, 1)
            GPIO.output(genel.sol_motorlar_one_hareket_pini, 1)
            GPIO.output(genel.sag_motorlar_arkaya_hareket_pini, 0)
            GPIO.output(genel.sol_motorlar_arkaya_hareket_pini, 0)
            genel.arka_fren_lambalarini_sondur()
            genel.arka_geri_vites_lambasini_sondur()        
            genel.arac_hareket_halinde_mi   = True
            genel.aracin_yonu               = "İleri Sol"
        else:
            genel.arac_durdu()           
            print("\n****** ARACIN HAREKET EDECEĞİ YÖNDE KRİTİK MESAFEDE NESNE ALGILANDI, ARAÇ HAREKET ETTİRİLMEDİ\n")

    def arac_ileri_saga_donuyor():
        genel.yanan_sinyal = "Sağ Sinyaller Yanıyor"
        if (not genel.arac_hareket_halinde_mi and "ön-orta" not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler and \
            "ön-sağ" not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler) or (genel.arac_hareket_halinde_mi and \
            "ön-orta" not in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler and \
            "ön-sağ" not in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler):
            genel.sag_motorlar_pwm.ChangeDutyCycle(genel.sag_motor_hizi)
            genel.sol_motorlar_pwm.ChangeDutyCycle(genel.sol_motor_hizi)        
            GPIO.output(genel.sag_motorlar_one_hareket_pini, 1)
            GPIO.output(genel.sol_motorlar_one_hareket_pini, 1)
            GPIO.output(genel.sag_motorlar_arkaya_hareket_pini, 0)
            GPIO.output(genel.sol_motorlar_arkaya_hareket_pini, 0)
            genel.arka_fren_lambalarini_sondur()
            genel.arka_geri_vites_lambasini_sondur()        
            genel.arac_hareket_halinde_mi   = True
            genel.aracin_yonu               = "İleri Sağ"
        else:
            genel.arac_durdu()            
            print("\n****** ARACIN HAREKET EDECEĞİ YÖNDE KRİTİK MESAFEDE NESNE ALGILANDI, ARAÇ HAREKET ETTİRİLMEDİ\n")

    def arac_geri_sola_donuyor():
        genel.yanan_sinyal = "Sol Sinyaller Yanıyor"
        if (not genel.arac_hareket_halinde_mi and "arka-orta" not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler and \
            "arka-sol" not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler) or (genel.arac_hareket_halinde_mi and \
            "arka-orta" not in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler and \
            "arka-sol" not in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler):
            genel.sag_motorlar_pwm.ChangeDutyCycle(genel.sag_motor_hizi)
            genel.sol_motorlar_pwm.ChangeDutyCycle(genel.sol_motor_hizi)
            GPIO.output(genel.sag_motorlar_one_hareket_pini, 0)
            GPIO.output(genel.sol_motorlar_one_hareket_pini, 0)
            GPIO.output(genel.sag_motorlar_arkaya_hareket_pini, 1)
            GPIO.output(genel.sol_motorlar_arkaya_hareket_pini, 1)
            genel.arka_fren_lambalarini_sondur()
            genel.arka_geri_vites_lambasini_yak()        
            genel.arac_hareket_halinde_mi   = True
            genel.aracin_yonu               = "Geri Sol"
        else:
            genel.arac_durdu()            
            print("\n****** ARACIN HAREKET EDECEĞİ YÖNDE KRİTİK MESAFEDE NESNE ALGILANDI, ARAÇ HAREKET ETTİRİLMEDİ\n")

    def arac_geri_saga_donuyor():
        genel.yanan_sinyal = "Sağ Sinyaller Yanıyor"
        if (not genel.arac_hareket_halinde_mi and "arka-orta" not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler and \
            "arka-sağ" not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler) or (genel.arac_hareket_halinde_mi and \
            "arka-orta" not in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler and \
            "arka-sağ" not in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler):
            genel.sag_motorlar_pwm.ChangeDutyCycle(genel.sag_motor_hizi)
            genel.sol_motorlar_pwm.ChangeDutyCycle(genel.sol_motor_hizi)        
            GPIO.output(genel.sag_motorlar_one_hareket_pini, 0)
            GPIO.output(genel.sol_motorlar_one_hareket_pini, 0)
            GPIO.output(genel.sag_motorlar_arkaya_hareket_pini, 1)
            GPIO.output(genel.sol_motorlar_arkaya_hareket_pini, 1)
            genel.arka_fren_lambalarini_sondur()
            genel.arka_geri_vites_lambasini_yak()        
            genel.arac_hareket_halinde_mi   = True
            genel.aracin_yonu               = "Geri Sağ"
        else:
            genel.arac_durdu()            
            print("\n****** ARACIN HAREKET EDECEĞİ YÖNDE KRİTİK MESAFEDE NESNE ALGILANDI, ARAÇ HAREKET ETTİRİLMEDİ\n")

    def arac_tam_saga_donuyor():
        genel.yanan_sinyal = "Sağ Sinyaller Yanıyor"
        if (not genel.arac_hareket_halinde_mi and "sağ" not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler) or \
        (genel.arac_hareket_halinde_mi and "sağ" not in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler):
            genel.sag_motorlar_pwm.ChangeDutyCycle(genel.sag_motor_hizi)
            genel.sol_motorlar_pwm.ChangeDutyCycle(genel.sol_motor_hizi)        
            GPIO.output(genel.sag_motorlar_one_hareket_pini, 0)
            GPIO.output(genel.sol_motorlar_one_hareket_pini, 1)
            GPIO.output(genel.sag_motorlar_arkaya_hareket_pini, 1)
            GPIO.output(genel.sol_motorlar_arkaya_hareket_pini, 0)
            genel.arka_fren_lambalarini_sondur()
            genel.arka_geri_vites_lambasini_sondur()
            genel.arac_hareket_halinde_mi   = True
            genel.aracin_yonu               = "Tam Sağ"
        else:
            genel.arac_durdu()           
            print("\n****** ARACIN HAREKET EDECEĞİ YÖNDE KRİTİK MESAFEDE NESNE ALGILANDI, ARAÇ HAREKET ETTİRİLMEDİ\n")

    def arac_tam_sola_donuyor():
        genel.yanan_sinyal = "Sol Sinyaller Yanıyor"
        if (not genel.arac_hareket_halinde_mi and "sol" not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler) or \
        (genel.arac_hareket_halinde_mi and "sol" not in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler):
            genel.sag_motorlar_pwm.ChangeDutyCycle(genel.sag_motor_hizi)
            genel.sol_motorlar_pwm.ChangeDutyCycle(genel.sol_motor_hizi)
            GPIO.output(genel.sag_motorlar_one_hareket_pini, 1)
            GPIO.output(genel.sol_motorlar_one_hareket_pini, 0)
            GPIO.output(genel.sag_motorlar_arkaya_hareket_pini, 0)
            GPIO.output(genel.sol_motorlar_arkaya_hareket_pini, 1)
            genel.arka_fren_lambalarini_sondur()
            genel.arka_geri_vites_lambasini_sondur()
            genel.arac_hareket_halinde_mi   = True
            genel.aracin_yonu               = "Tam Sol"
        else:
            genel.arac_durdu()
            print("\n****** ARACIN HAREKET EDECEĞİ YÖNDE KRİTİK MESAFEDE NESNE ALGILANDI, ARAÇ HAREKET ETTİRİLMEDİ\n")

    def arka_fren_lambalarini_yak():
        GPIO.output(genel.arka_orta_kirmizi_parlak_fren_lambalari_kontrol_pini, 1)
        genel.fren_lambasi_durumu = "Fren lambaları yanıyor"

    def arka_fren_lambalarini_sondur():
        GPIO.output(genel.arka_orta_kirmizi_parlak_fren_lambalari_kontrol_pini, 0)
        genel.fren_lambasi_durumu = "Fren lambaları sönük"

    def arka_alt_kirmizi_kisa_stop_lambalarini_yak():
        GPIO.output(genel.arka_alt_kirmizi_kisa_stop_lambalar_kontrol_pini, 1)

    def arka_alt_kirmizi_kisa_stop_lambalarini_sondur():
        GPIO.output(genel.arka_alt_kirmizi_kisa_stop_lambalar_kontrol_pini, 0)

    def arka_fren_lambalarini_yak_sondur_yak():
        genel.arka_fren_lambalarini_yak()
        time.sleep(0.2)
        genel.arka_fren_lambalarini_sondur()
        time.sleep(0.2)
        genel.arka_fren_lambalarini_yak()
        time.sleep(0.2)
        genel.arka_fren_lambalarini_sondur()
        time.sleep(0.2)
        genel.arka_fren_lambalarini_yak()

    def stop_lambalarini_yak():
        genel.arka_alt_kirmizi_kisa_stop_lambalarini_yak()
        genel.on_alt_kisa_stop_lambalarini_yak()
        genel.stop_lambalarinin_durumu = "Stop lambaları yanıyor"        

    def stop_lambalarini_sondur():
        genel.arka_alt_kirmizi_kisa_stop_lambalarini_sondur()
        genel.on_alt_kisa_stop_lambalarini_sondur()
        genel.stop_lambalarinin_durumu = "Stop lambaları sönük"        

    def on_alt_kisa_stop_lambalarini_yak():
        GPIO.output(genel.on_alt_kisa_beyaz_stop_lambalar_kontrol_pini, 1)

    def on_alt_kisa_stop_lambalarini_sondur():
        GPIO.output(genel.on_alt_kisa_beyaz_stop_lambalar_kontrol_pini, 0)

    def on_ust_uzun_farlari_yak():
        GPIO.output(genel.on_ust_uzun_beyaz_farlar_kontrol_pini, 1)
        genel.uzun_farlarin_durumu = "Uzun farlar yanıyor"

    def on_ust_uzun_farlari_sondur():
        GPIO.output(genel.on_ust_uzun_beyaz_farlar_kontrol_pini, 0)
        genel.uzun_farlarin_durumu = "Uzun farlar sönük"

    def arka_geri_vites_lambasini_yak():
        GPIO.output(genel.arka_ust_tek_beyaz_geri_vites_lambasi_kontrol_pini, 1)
        genel.geri_vites_lambasi_durumu = "Geri vites lambası yanıyor"

    def arka_geri_vites_lambasini_sondur():
        GPIO.output(genel.arka_ust_tek_beyaz_geri_vites_lambasi_kontrol_pini, 0)
        genel.geri_vites_lambasi_durumu = "Geri vites lambası sönük"

    def sol_sinyalleri_yak():
        genel.on_sol_sari_sinyal_lambasini_yak()
        genel.arka_sol_sari_sinyal_lambasini_yak()

    def sol_sinyalleri_sondur():
        genel.on_sol_sari_sinyal_lambasini_sondur()
        genel.arka_sol_sari_sinyal_lambasini_sondur()

    def sag_sinyalleri_yak():
        genel.on_sag_sari_sinyal_lambasini_yak()
        genel.arka_sag_sari_sinyal_lambasini_yak()

    def sag_sinyalleri_sondur():
        genel.on_sag_sari_sinyal_lambasini_sondur()
        genel.arka_sag_sari_sinyal_lambasini_sondur()

    def on_sol_sari_sinyal_lambasini_yak():
        GPIO.output(genel.on_sol_sari_sinyal_fari_kontrol_pini, 1)

    def on_sol_sari_sinyal_lambasini_sondur():
        GPIO.output(genel.on_sol_sari_sinyal_fari_kontrol_pini, 0)

    def on_sag_sari_sinyal_lambasini_yak():
        GPIO.output(genel.on_sag_sari_sinyal_fari_kontrol_pini, 1)

    def on_sag_sari_sinyal_lambasini_sondur():
        GPIO.output(genel.on_sag_sari_sinyal_fari_kontrol_pini, 0)

    def arka_sol_sari_sinyal_lambasini_yak():
        GPIO.output(genel.arka_sol_sari_sinyal_fari_kontrol_pini, 1)

    def arka_sol_sari_sinyal_lambasini_sondur():
        GPIO.output(genel.arka_sol_sari_sinyal_fari_kontrol_pini, 0)

    def arka_sag_sari_sinyal_lambasini_yak():
        GPIO.output(genel.arka_sag_sari_sinyal_fari_kontrol_pini, 1)

    def arka_sag_sari_sinyal_lambasini_sondur():
        GPIO.output(genel.arka_sag_sari_sinyal_fari_kontrol_pini, 0)

    def tum_farlari_yak():
        genel.stop_lambalarini_yak()
        genel.on_ust_uzun_farlari_yak()
        genel.arka_fren_lambalarini_yak()
        genel.arka_geri_vites_lambasini_yak()
        genel.sol_sinyalleri_yak()
        genel.sag_sinyalleri_yak()

    def tum_farlari_sondur():
        genel.stop_lambalarini_sondur()
        genel.on_ust_uzun_farlari_sondur()
        genel.arka_fren_lambalarini_sondur()
        genel.arka_geri_vites_lambasini_sondur()
        genel.sol_sinyalleri_sondur()
        genel.sag_sinyalleri_sondur()


    def disco_mode_on():
        sure = 0.08
        genel.arac_durdu()
        uzunlar_btn.config(relief=RAISED)
        kisalar_btn.config(relief=RAISED)
        selektor_btn.config(relief=RAISED)
        for i in range(3):
            genel.tum_farlari_sondur()
            genel.on_sol_sari_sinyal_lambasini_yak()
            time.sleep(sure)
            genel.on_alt_kisa_stop_lambalarini_yak()
            time.sleep(sure)
            genel.on_ust_uzun_farlari_yak()
            genel.on_sol_sari_sinyal_lambasini_sondur()
            time.sleep(sure)        
            genel.on_sag_sari_sinyal_lambasini_yak()
            genel.on_alt_kisa_stop_lambalarini_sondur()
            time.sleep(sure)        
            genel.arka_sag_sari_sinyal_lambasini_yak()
            genel.on_ust_uzun_farlari_sondur()            
            time.sleep(sure)
            genel.arka_alt_kirmizi_kisa_stop_lambalarini_yak()
            genel.on_sag_sari_sinyal_lambasini_sondur()            
            time.sleep(sure)
            genel.arka_fren_lambalarini_yak()
            genel.arka_sag_sari_sinyal_lambasini_sondur()
            time.sleep(sure)
            genel.arka_geri_vites_lambasini_yak()
            genel.arka_alt_kirmizi_kisa_stop_lambalarini_sondur()            
            time.sleep(sure)
            genel.arka_sol_sari_sinyal_lambasini_yak()
            genel.arka_fren_lambalarini_sondur()            
            time.sleep(sure)
            genel.arka_geri_vites_lambasini_sondur()
            time.sleep(sure)
            genel.arka_sol_sari_sinyal_lambasini_sondur()

        
    def multiplexer_channel_and_value_set_function(pin, durum, *args):
        if pin == "C0":
            GPIO.output(genel.multiplexer_SO_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S1_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S2_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S3_kontrol_pini, 0)
        elif pin == "C1":
            GPIO.output(genel.multiplexer_SO_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S1_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S2_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S3_kontrol_pini, 0)
        elif pin == "C2":
            GPIO.output(genel.multiplexer_SO_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S1_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S2_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S3_kontrol_pini, 0)
        elif pin == "C3":
            GPIO.output(genel.multiplexer_SO_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S1_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S2_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S3_kontrol_pini, 0)
        elif pin == "C4":
            GPIO.output(genel.multiplexer_SO_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S1_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S2_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S3_kontrol_pini, 0)
        elif pin == "C5":
            GPIO.output(genel.multiplexer_SO_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S1_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S2_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S3_kontrol_pini, 0)
        elif pin == "C6":
            GPIO.output(genel.multiplexer_SO_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S1_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S2_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S3_kontrol_pini, 0)
        elif pin == "C7":
            GPIO.output(genel.multiplexer_SO_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S1_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S2_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S3_kontrol_pini, 0)
        elif pin == "C8":
            GPIO.output(genel.multiplexer_SO_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S1_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S2_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S3_kontrol_pini, 1)
        elif pin == "C9":
            GPIO.output(genel.multiplexer_SO_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S1_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S2_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S3_kontrol_pini, 1)
        elif pin == "C10":
            GPIO.output(genel.multiplexer_SO_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S1_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S2_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S3_kontrol_pini, 1)
        elif pin == "C11":
            GPIO.output(genel.multiplexer_SO_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S1_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S2_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S3_kontrol_pini, 1)
        elif pin == "C12":
            GPIO.output(genel.multiplexer_SO_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S1_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S2_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S3_kontrol_pini, 1)
        elif pin == "C13":
            GPIO.output(genel.multiplexer_SO_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S1_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S2_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S3_kontrol_pini, 1)
        elif pin == "C14":
            GPIO.output(genel.multiplexer_SO_kontrol_pini, 0)
            GPIO.output(genel.multiplexer_S1_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S2_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S3_kontrol_pini, 1)                                                                        
        elif pin == "C15":
            GPIO.output(genel.multiplexer_SO_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S1_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S2_kontrol_pini, 1)
            GPIO.output(genel.multiplexer_S3_kontrol_pini, 1)

        if durum:
            GPIO.output(genel.multiplexer_SIG_kontrol_pini, 1)
        else:
            GPIO.output(genel.multiplexer_SIG_kontrol_pini, 0)


    def selektor_yap():
        selektor_btn.config(relief=SUNKEN)
        neo_car_gui.update_idletasks()
        selektor_on_ust_lambalarin_durumu = GPIO.input(genel.on_ust_uzun_beyaz_farlar_kontrol_pini)

        for i in range(2):
            genel.on_ust_uzun_farlari_yak()
            time.sleep(0.2)
            genel.on_ust_uzun_farlari_sondur()
            time.sleep(0.2)

        if selektor_on_ust_lambalarin_durumu: genel.on_ust_uzun_farlari_yak()

        del selektor_on_ust_lambalarin_durumu

        selektor_btn.config(relief=RAISED)
        neo_car_gui.update_idletasks()        

    def programi_sonlandir(*args):
        genel.arac_durdu()
        genel.otomatik_mesafe_olcum_thread_calissin_mi   = False
        genel.sinyal_thread_calissin_mi                  = False
        genel.klavyeden_motor_kontrol_thread_calissin_mi = False
        msg_lbl.after_cancel(genel.kontrol_cevrimi_after_id)
        genel.video.release()
        cv2.destroyAllWindows()
        neo_car_gui.destroy()


    def sinyal_thread():
        while genel.sinyal_thread_calissin_mi:
            while genel.yanan_sinyal == "Sol Sinyaller Yanıyor" or genel.yanan_sinyal == "Sağ Sinyaller Yanıyor" or genel.yanan_sinyal == "Dörtlü Sinyaller Yanıyor":
                if genel.yanan_sinyal == "Sol Sinyaller Yanıyor":
                    #print("Sol sinyaller yanıyor")
                    genel.sol_sinyalleri_yak()
                    time.sleep(genel.sinyal_yanma_suresi)
                    genel.sol_sinyalleri_sondur()
                    time.sleep(genel.sinyal_sonme_suresi - 0.1)
                elif genel.yanan_sinyal == "Sağ Sinyaller Yanıyor":
                    #print("Sağ sinyaller yanıyor")
                    genel.sag_sinyalleri_yak()
                    time.sleep(genel.sinyal_yanma_suresi)
                    genel.sag_sinyalleri_sondur()
                    time.sleep(genel.sinyal_sonme_suresi - 0.1)
                elif genel.yanan_sinyal == "Dörtlü Sinyaller Yanıyor":
                    #print("Dörlü sinyaller yanıyor")
                    genel.sag_sinyalleri_yak()
                    genel.sol_sinyalleri_yak()
                    time.sleep(genel.sinyal_yanma_suresi)
                    genel.sag_sinyalleri_sondur()
                    genel.sol_sinyalleri_sondur()
                    time.sleep(genel.sinyal_sonme_suresi)
            if genel.yanan_sinyal == "Sinyaller Yanmıyor":
                #print("Sinyaller Yanmıyor")
                pass
            time.sleep(0.1)


    def otomatik_mesafe_olcum():
        while genel.otomatik_mesafe_olcum_thread_calissin_mi:
            for sira in range(len(genel.mesafe_sensorleri_adlari)):
                # önce tüm mesafe sensörleri trigger pin'lerini low yapıyoruz
                for k in genel.mesafe_sensorleri_trigger_pinleri:
                    genel.multiplexer_channel_and_value_set_function(k, 0)

                sensor_tek_seferde_olcum_degerleri = []
                for i in range(genel.mesafe_sensoru_tek_seferde_olcum_sayisi):
                    pulse_start_time    = None
                    pulse_end_time      = None
                    pulse_duration      = None
                    distance            = None
                    pulse_start_i_beklemeye_baslama_zamani = None
                    pulse_end_i_beklemeye_baslama_zamani = None
                    # ölçüm yapacağımız mesafe sensörünün trigger pinini 20 mikro saniye süreyle high yapıyoruz\
                    # yani 20 mikro saniye sinyal gönderiyoruz, sonra tekrar low yapıyoruz
                    genel.multiplexer_channel_and_value_set_function(genel.mesafe_sensorleri_trigger_pinleri[sira], 1)
                    time.sleep(0.00002)
                    genel.multiplexer_channel_and_value_set_function(genel.mesafe_sensorleri_trigger_pinleri[sira], 0)

                    # mesafe sensörünün echo pininin sinyali almaya başlamasını bekliyoruz, sinyali aldığı andan önceki anı\
                    # sinyali alışın başlangıç zamanı olarak keydediyoruz
                    pulse_start_i_beklemeye_baslama_zamani = datetime.datetime.now()
                    while GPIO.input(genel.mesafe_sensorleri_echo_pinleri[sira]) == 0:
                        pulse_start_time = datetime.datetime.now()
                        if datetime.datetime.now() - pulse_start_i_beklemeye_baslama_zamani >= datetime.timedelta(milliseconds=5):
                            break

                    # sinyali almaya başladıktan sonra bitirmesini bekliyor ve bitirdiği anı kaydediyoruz
                    if pulse_start_time is not None:
                        pulse_end_i_beklemeye_baslama_zamani = datetime.datetime.now()
                        while GPIO.input(genel.mesafe_sensorleri_echo_pinleri[sira]) == 1:
                            pulse_end_time = datetime.datetime.now()
                            if datetime.datetime.now() - pulse_end_i_beklemeye_baslama_zamani >= datetime.timedelta(milliseconds=5):
                                break

                    if pulse_start_time is not None and pulse_end_time is not None:
                        distance = round((pulse_end_time - pulse_start_time).total_seconds() * 17150, 2)
                        sensor_tek_seferde_olcum_degerleri.append(distance)

                    if sensor_tek_seferde_olcum_degerleri == []:
                        genel.aracin_cevredeki_nesnelerle_mesafeleri[genel.mesafe_sensorleri_adlari[sira]] = 0
                    else:
                        genel.aracin_cevredeki_nesnelerle_mesafeleri[genel.mesafe_sensorleri_adlari[sira]] = int(sum(sensor_tek_seferde_olcum_degerleri)/len(sensor_tek_seferde_olcum_degerleri))

                if 0 < genel.aracin_cevredeki_nesnelerle_mesafeleri[genel.mesafe_sensorleri_adlari[sira]] <= genel.arac_dururken_mesafe_olcumu_kritik_deger:
                    if genel.mesafe_sensorleri_adlari[sira] not in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler:
                        genel.arac_dururken_kritik_mesafede_nesne_olan_yonler.append(genel.mesafe_sensorleri_adlari[sira])
                    if genel.mesafe_sensorleri_adlari[sira] not in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler:
                        genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler.append(genel.mesafe_sensorleri_adlari[sira])
                elif genel.arac_dururken_mesafe_olcumu_kritik_deger < genel.aracin_cevredeki_nesnelerle_mesafeleri[genel.mesafe_sensorleri_adlari[sira]] <= \
                genel.arac_hareket_halindeyken_mesafe_olcumu_kritik_deger:
                    if genel.mesafe_sensorleri_adlari[sira] in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler:
                        genel.arac_dururken_kritik_mesafede_nesne_olan_yonler.remove(genel.mesafe_sensorleri_adlari[sira])
                    if genel.mesafe_sensorleri_adlari[sira] not in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler:
                        genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler.append(genel.mesafe_sensorleri_adlari[sira])
                elif genel.aracin_cevredeki_nesnelerle_mesafeleri[genel.mesafe_sensorleri_adlari[sira]] > genel.arac_hareket_halindeyken_mesafe_olcumu_kritik_deger:
                    if genel.mesafe_sensorleri_adlari[sira] in genel.arac_dururken_kritik_mesafede_nesne_olan_yonler:
                        genel.arac_dururken_kritik_mesafede_nesne_olan_yonler.remove(genel.mesafe_sensorleri_adlari[sira])
                    if genel.mesafe_sensorleri_adlari[sira] in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler:
                        genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler.remove(genel.mesafe_sensorleri_adlari[sira])

                if genel.arac_hareket_halinde_mi:
                    if (genel.aracin_yonu == "Düz İleri" and "ön-orta" in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler) or \
                    (genel.aracin_yonu == "Düz Geri" and "arka-orta" in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler) or \
                    (genel.aracin_yonu == "İleri Sol" and ("ön-orta" in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler or \
                        "ön-sol" in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler)) or \
                    (genel.aracin_yonu == "İleri Sağ" and ("ön-orta" in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler or \
                        "ön-sağ" in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler)) or \
                    (genel.aracin_yonu == "Geri Sol" and ("arka-orta" in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler or \
                        "arka-sol" in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler)) or \
                    (genel.aracin_yonu == "Geri Sağ" and ("arka-orta" in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler or \
                        "arka-sağ" in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler)) or \
                    (genel.aracin_yonu == "Tam Sağ" and "sağ" in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler) or \
                    (genel.aracin_yonu == "Tam Sol" and "sol" in genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler):
                        print("\n****** ARACIN HAREKET ETTİĞİ YÖNDE KRİTİK MESAFEDE NESNE ALGILANDI ARAÇ DURDURULDU")
                        genel.arac_durdu()
                        genel.arka_fren_lambalarini_yak_sondur_yak()


            # ekranda mesafe label'i içine kritik mesafede nesne algılandıysa kırmızı ile mesafeleri yazdırmak
            # algılanmadıysa siyahla yazdırmak için bu kısmı yaptım
            if genel.arac_hareket_halinde_mi:
                if genel.arac_hareket_halindeyken_kritik_mesafede_nesne_olan_yonler == []:
                    genel.kritik_mesafede_engel_algilandi_mi = False
                else:
                    genel.kritik_mesafede_engel_algilandi_mi = True
            else:
                if genel.arac_dururken_kritik_mesafede_nesne_olan_yonler == []:                
                    genel.kritik_mesafede_engel_algilandi_mi = False
                else:
                    genel.kritik_mesafede_engel_algilandi_mi = True

            #print(genel.aracin_cevredeki_nesnelerle_mesafeleri)
            time.sleep(0.3)


    def kisa_far_kontrolu():
        if genel.stop_lambalarinin_durumu == "Stop lambaları yanıyor":
            genel.stop_lambalarini_sondur()
            kisalar_btn.config(relief=RAISED)
            #stop lambalarını söndürdüğümüzde ön üst uzun farları da söndürüyoruz
            genel.on_ust_uzun_farlari_sondur()
            uzunlar_btn.config(relief=RAISED)
        else:
            genel.stop_lambalarini_yak()
            kisalar_btn.config(relief=SUNKEN)


    def uzun_far_kontrolu():
        if genel.uzun_farlarin_durumu == "Uzun farlar yanıyor":
            genel.on_ust_uzun_farlari_sondur()
            uzunlar_btn.config(relief=RAISED)
        else:
            # uzunları yaktığımızda kısalar yanmıyorsa otomatik onların da yanması lazım
            genel.stop_lambalarini_yak()
            kisalar_btn.config(relief=SUNKEN)
            genel.on_ust_uzun_farlari_yak()
            uzunlar_btn.config(relief=SUNKEN)           


    def disco_mode_kontrolu():
        disco_mode_btn.config(relief=SUNKEN)
        neo_car_gui.update_idletasks()
        genel.disco_mode_on()
        disco_mode_btn.config(relief=RAISED)
        neo_car_gui.update_idletasks()


    def dortlu_sinyal_kontrolu():
        if genel.yanan_sinyal == "Dörtlü Sinyaller Yanıyor":
            dortluler_btn.config(relief=RAISED)
            neo_car_gui.update_idletasks()
            genel.yanan_sinyal = "Sinyaller Yanmıyor"
        else:
            genel.yanan_sinyal = "Dörtlü Sinyaller Yanıyor"        
            dortluler_btn.config(relief=SUNKEN)
            neo_car_gui.update_idletasks()            

    '''
    Manuel sürüşteyken klavyeden aracın hareketi ve ışıkları ile ilgili tuşlara basılınca dict içinde o tuşun değeri 1 oluyor
    bu dict içinde 1 olan tuşa göre araç hareket ettiriliyor
    tuş bırakıldığında tuş bırakma zamanlarının tutulduğu dict o an güncelleniyor
    tuş bırakıldıktan sonra 200 milisaniye geçti ise o tuş bırakılmış sayılıyor ve tekrar dict te o tuş 0 yapılıyor
    bu 200 milisaniyeyi koymamızın sebebi özellikle VNC ile bağlı çalışırken uzun süreli tuş basımlarında
    Raspberry kendisi sürekli tuşu basmış ve bırakmış olarak görüyor, halbuki o anda tuşa basılı durumda
    bu da motorların kontrollerini imkansız hale getiriyor.
    Şimdi tuşa basıldığı ve bırakıldığı anı tam olarak yakalayabiliyoruz

    '''

    def tus_basma_kontrol(event):
        if (event.keysym == "q" or event.keysym == "Q") and genel.kontrol_tuslari_basma_durumlari_simdiki["q"] == 0:
            genel.kontrol_tuslari_basma_durumlari_simdiki["q"] = 1
        elif (event.keysym == "w" or event.keysym == "W") and genel.kontrol_tuslari_basma_durumlari_simdiki["w"] == 0:
            genel.kontrol_tuslari_basma_durumlari_simdiki["w"] = 1
        elif event.keysym == "Up" and genel.kontrol_tuslari_basma_durumlari_simdiki["Up"] == 0:
            genel.kontrol_tuslari_basma_durumlari_simdiki["Up"] = 1
        elif (event.keysym == "e" or event.keysym == "E") and genel.kontrol_tuslari_basma_durumlari_simdiki["e"] == 0:
            genel.kontrol_tuslari_basma_durumlari_simdiki["e"] = 1
        elif (event.keysym == "a" or event.keysym == "A") and genel.kontrol_tuslari_basma_durumlari_simdiki["a"] == 0:
            genel.kontrol_tuslari_basma_durumlari_simdiki["a"] = 1
        elif event.keysym == "Left" and genel.kontrol_tuslari_basma_durumlari_simdiki["Left"] == 0:
            genel.kontrol_tuslari_basma_durumlari_simdiki["Left"] = 1
        elif (event.keysym == "s" or event.keysym == "S" or event.keysym == "space") and genel.kontrol_tuslari_basma_durumlari_simdiki["s-space"] == 0:
            genel.kontrol_tuslari_basma_durumlari_simdiki["s-space"] = 1
        elif (event.keysym == "d" or event.keysym == "D") and genel.kontrol_tuslari_basma_durumlari_simdiki["d"] == 0:
            genel.kontrol_tuslari_basma_durumlari_simdiki["d"] = 1
        elif event.keysym == "Right" and genel.kontrol_tuslari_basma_durumlari_simdiki["Right"] == 0:
            genel.kontrol_tuslari_basma_durumlari_simdiki["Right"] = 1
        elif (event.keysym == "z" or event.keysym == "Z") and genel.kontrol_tuslari_basma_durumlari_simdiki["z"] == 0:
            genel.kontrol_tuslari_basma_durumlari_simdiki["z"] = 1 
        elif (event.keysym == "x" or event.keysym == "X") and genel.kontrol_tuslari_basma_durumlari_simdiki["x"] == 0:
            genel.kontrol_tuslari_basma_durumlari_simdiki["x"] = 1
        elif event.keysym == "Down" and genel.kontrol_tuslari_basma_durumlari_simdiki["Down"] == 0:
            genel.kontrol_tuslari_basma_durumlari_simdiki["Down"] = 1
        elif (event.keysym == "c" or event.keysym == "C") and genel.kontrol_tuslari_basma_durumlari_simdiki["c"] == 0:
            genel.kontrol_tuslari_basma_durumlari_simdiki["c"] = 1
        elif event.keysym == "1":
            kisalar_btn.config(relief=SUNKEN)
            genel.kisa_far_kontrolu()
        elif event.keysym == "2":
            uzunlar_btn.config(relief=SUNKEN)
            genel.uzun_far_kontrolu()
        elif event.keysym == "3":
            selektor_btn.config(relief=SUNKEN)
            genel.selektor_yap()
        elif event.keysym == "7":
            genel.disco_mode_kontrolu()
        elif event.keysym == "9":
            genel.dortlu_sinyal_kontrolu()
                


    def tus_birakma_zaman_takip(event):
        tusun_birakildigi_an = datetime.datetime.now()
        
        if event.keysym == "q" or event.keysym == "Q":
            genel.kontrol_tuslari_birakma_zamanlari["q"] = tusun_birakildigi_an
        elif event.keysym == "w" or event.keysym == "W":
            genel.kontrol_tuslari_birakma_zamanlari["w"] = tusun_birakildigi_an
        elif event.keysym == "Up":
            genel.kontrol_tuslari_birakma_zamanlari["Up"] = tusun_birakildigi_an
        elif event.keysym == "e" or event.keysym == "E":
            genel.kontrol_tuslari_birakma_zamanlari["e"] = tusun_birakildigi_an
        elif event.keysym == "a" or event.keysym == "A":
            genel.kontrol_tuslari_birakma_zamanlari["a"] = tusun_birakildigi_an
        elif event.keysym == "Left":
            genel.kontrol_tuslari_birakma_zamanlari["Left"] = tusun_birakildigi_an
        elif event.keysym == "s" or event.keysym == "S" or event.keysym == "space":
            genel.kontrol_tuslari_birakma_zamanlari["s-space"] = tusun_birakildigi_an
        elif event.keysym == "d" or event.keysym == "D":
            genel.kontrol_tuslari_birakma_zamanlari["d"] = tusun_birakildigi_an
        elif event.keysym == "Right":
            genel.kontrol_tuslari_birakma_zamanlari["Right"] = tusun_birakildigi_an            
        elif event.keysym == "z" or event.keysym == "Z":
            genel.kontrol_tuslari_birakma_zamanlari["z"] = tusun_birakildigi_an
        elif event.keysym == "x" or event.keysym == "X":
            genel.kontrol_tuslari_birakma_zamanlari["x"] = tusun_birakildigi_an
        elif event.keysym == "Down":
            genel.kontrol_tuslari_birakma_zamanlari["Down"] = tusun_birakildigi_an            
        elif event.keysym == "c" or event.keysym == "C":
            genel.kontrol_tuslari_birakma_zamanlari["c"] = tusun_birakildigi_an


    def tuslarin_durumu_ile_motor_kontrol():   #tuşların durumunun kontrolü için açılış aşamasında thread olarak çalıştırılıyor
        tus_birakma_sonrasi_kontrol_icin_gecen_sure = datetime.timedelta(milliseconds=200)
        while genel.klavyeden_motor_kontrol_thread_calissin_mi :
            for key, value in genel.kontrol_tuslari_birakma_zamanlari.items():
                if datetime.datetime.now() >= value + tus_birakma_sonrasi_kontrol_icin_gecen_sure:
                    genel.kontrol_tuslari_birakma_zamanlari[key] = datetime.datetime(2100, 1, 1, 0, 0)
                    genel.kontrol_tuslari_basma_durumlari_simdiki[key] = 0

            if genel.kontrol_tuslari_basma_durumlari_simdiki != genel.kontrol_tuslari_basma_durumlari_onceki:

                #print(genel.kontrol_tuslari_basma_durumlari_simdiki)
                if genel.kontrol_tuslari_basma_durumlari_simdiki == {"q": 0, "w": 0, "Up": 0, "e": 0, "a": 0, "Left": 0, "s-space": 0, "d": 0, "Right": 0, "z": 0, \
                                                                     "x": 0, "Down": 0, "c": 0}:
                    sol_ust_ok_btn.config(relief=RAISED)
                    yukari_btn.config(relief=RAISED)
                    sag_ust_ok_btn.config(relief=RAISED)
                    sol_ok_btn.config(relief=RAISED)
                    stop_btn.config(relief=RAISED)
                    sag_ok_btn.config(relief=RAISED)                    
                    sol_alt_ok_btn.config(relief=RAISED)
                    asagi_btn.config(relief=RAISED)
                    sag_alt_ok_btn.config(relief=RAISED)
                    genel.arac_durdu()
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["q"] == 1:
                    sol_ust_ok_btn.config(relief=SUNKEN)
                    genel.sol_motor_hizi = 40
                    genel.sag_motor_hizi = 55
                    genel.arac_tam_sola_donuyor()
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["w"] == 1:
                    yukari_btn.config(relief=SUNKEN)
                    genel.sol_motor_hizi = 50
                    genel.sag_motor_hizi = 50                        
                    genel.arac_duz_ileri_gidiyor()
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["Up"] == 1:
                    yukari_btn.config(relief=SUNKEN)
                    genel.sol_motor_hizi = 60
                    genel.sag_motor_hizi = 60                        
                    genel.arac_duz_ileri_gidiyor()                        
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["e"] == 1:
                    sag_ust_ok_btn.config(relief=SUNKEN)
                    genel.sag_motor_hizi = 40 
                    genel.sol_motor_hizi = 55
                    genel.arac_tam_saga_donuyor()
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["a"] == 1:
                    sol_ok_btn.config(relief=SUNKEN)
                    genel.sol_motor_hizi = 50 
                    genel.sag_motor_hizi = 50                        
                    genel.arac_tam_sola_donuyor()
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["Left"] == 1:
                    sol_ok_btn.config(relief=SUNKEN)
                    genel.sol_motor_hizi = 60
                    genel.sag_motor_hizi = 60
                    genel.arac_tam_sola_donuyor()                        
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["s-space"] == 1:
                    stop_btn.config(relief=SUNKEN)
                    genel.arac_durdu()
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["d"] == 1:
                    sag_ok_btn.config(relief=SUNKEN)
                    genel.sag_motor_hizi = 50
                    genel.sol_motor_hizi = 50
                    genel.arac_tam_saga_donuyor()
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["Right"] == 1:
                    sag_ok_btn.config(relief=SUNKEN)
                    genel.sag_motor_hizi = 60 
                    genel.sol_motor_hizi = 60
                    genel.arac_tam_saga_donuyor()
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["z"] == 1:
                    sol_alt_ok_btn.config(relief=SUNKEN)
                    genel.sol_motor_hizi = 40
                    genel.sag_motor_hizi = 55                         
                    genel.arac_geri_sola_donuyor()
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["x"] == 1:
                    asagi_btn.config(relief=SUNKEN)
                    genel.sol_motor_hizi = 50
                    genel.sag_motor_hizi = 50                        
                    genel.arac_duz_geri_gidiyor()
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["Down"] == 1:
                    asagi_btn.config(relief=SUNKEN)
                    genel.sol_motor_hizi = 60
                    genel.sag_motor_hizi = 60                        
                    genel.arac_duz_geri_gidiyor()                        
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["c"] == 1:
                    sag_alt_ok_btn.config(relief=SUNKEN)
                    genel.sag_motor_hizi = 40 
                    genel.sol_motor_hizi = 55 
                    genel.arac_geri_saga_donuyor()                
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["q"] == 0:
                    sol_ust_ok_btn.config(relief=RAISED)
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["w"] == 0 or genel.kontrol_tuslari_basma_durumlari_simdiki["Up"] == 0:
                    yukari_btn.config(relief=RAISED)
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["e"] == 0:
                    sag_ust_ok_btn.config(relief=RAISED)
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["a"] == 0 or genel.kontrol_tuslari_basma_durumlari_simdiki["Left"] == 0:
                    sol_ok_btn.config(relief=RAISED)
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["s-space"] == 0:
                    stop_btn.config(relief=RAISED)
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["d"] == 0 or genel.kontrol_tuslari_basma_durumlari_simdiki["Right"] == 0:
                    sag_ok_btn.config(relief=RAISED)
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["z"] == 0:
                    sol_alt_ok_btn.config(relief=RAISED)
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["x"] == 0 or genel.kontrol_tuslari_basma_durumlari_simdiki["Down"] == 0:
                    asagi_btn.config(relief=RAISED)
                elif genel.kontrol_tuslari_basma_durumlari_simdiki["c"] == 0:
                    sag_alt_ok_btn.config(relief=RAISED)
                
                genel.kontrol_tuslari_basma_durumlari_onceki = genel.kontrol_tuslari_basma_durumlari_simdiki.copy()
        
        time.sleep(0.2)
    


    def equalize(img):
        img = cv2.equalizeHist(img)
        return img

    
    def grayscale(img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img

    
    def preprocessing(img):
        img = genel.grayscale(img)
        img = genel.equalize(img)
        img = img/255
        return img

     
    def getCalssName(classNo):
        if   classNo == 0: return 'Speed Limit 20 km/h'    
        elif classNo == 9: return 'No passing'
        elif classNo == 12: return 'Priority road'
        elif classNo == 13: return 'Yield'
        elif classNo == 14: return 'Stop'
        elif classNo == 38: return 'Keep right'
        elif classNo == 39: return 'Keep left'


    def kontrol_cevrimi():
        if genel.kritik_mesafede_engel_algilandi_mi:
            mesafe_lbl["fg"] = "red"
        else:
            mesafe_lbl["fg"] = "black"
        mesafe_lbl["text"] = str(genel.aracin_cevredeki_nesnelerle_mesafeleri).lstrip("{").rstrip("}").replace("'", "").replace(",", "  ")
        far_lbl['text']    = f"{genel.stop_lambalarinin_durumu} - {genel.uzun_farlarin_durumu} - {genel.fren_lambasi_durumu} - {genel.geri_vites_lambasi_durumu}"
        sinyal_lbl['text'] = genel.yanan_sinyal
        if genel.yanan_sinyal == "Dörtlü Sinyaller Yanıyor":
            dortluler_btn.config(relief=SUNKEN)
        else:
            dortluler_btn.config(relief=RAISED)
        
        ret, frame = genel.video.read()
        if ret:
            frame = cv2.flip(frame, -1)
            img   = np.asarray(frame)
            img   = cv2.resize(img, (32, 32))
            img   = genel.preprocessing(img)
            #cv2.imshow("Processed Image", img)
            img   = img.reshape(1, 32, 32, 1)
            cv2.putText(frame, "CLASS: " , (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, "PROBABILITY: ", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    
            # PREDICT IMAGE
            predictions      = model.predict(img)
            classIndex       = model.predict_classes(img)
            probabilityValue = np.amax(predictions)
            if probabilityValue > genel.detection_threshold:
                print(genel.getCalssName(classIndex))
                #cv2.rectangle(image, coordinate[0],coordinate[1], (0, 255, 0), 1)
                cv2.putText(frame, str(classIndex)+" "+str(genel.getCalssName(classIndex)), (120, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.putText(frame, str(round(probabilityValue*100,2) )+"%", (180, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2, cv2.LINE_AA)

                if genel.getCalssName(classIndex) != None:
                    msg_lbl["text"] = f"FPS : {genel.gerceklesen_frame_sayisi}/{genel.set_edilen_Fps}   -   Manuel Sürüş   -   {genel.getCalssName(classIndex)} Trafik Levhası Tespit Edildi"

                if genel.getCalssName(classIndex) == "Speed Limit 20 km/h":
                    #pass
                    genel.sol_motor_hizi = 70
                    genel.sag_motor_hizi = 70
                    genel.arac_duz_ileri_gidiyor()
                elif genel.getCalssName(classIndex) == "No passing" or genel.getCalssName(classIndex) == "Stop":
                    genel.arac_durdu()
                elif genel.getCalssName(classIndex) == "Keep right":
                    #pass
                    genel.sol_motor_hizi = 70
                    genel.sag_motor_hizi = 40
                    genel.arac_tam_saga_donuyor()
                elif genel.getCalssName(classIndex) == "Keep left":
                    #pass
                    genel.sol_motor_hizi = 40
                    genel.sag_motor_hizi = 70
                    genel.arac_tam_sola_donuyor()
                    
            else:
                msg_lbl["text"] = f"FPS : {genel.gerceklesen_frame_sayisi}/{genel.set_edilen_Fps}   -   Manuel Sürüş"

            cv2image          = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img               = Image.fromarray(cv2image)
            imgtk             = ImageTk.PhotoImage(image=img)
            goruntu_lbl.imgtk = imgtk
            goruntu_lbl.configure(image=imgtk)

            genel.saniyede_gerceklesen_frame_sayisi += 1

            # bu anı saniyeli olarak başlangıç değişkenine atıyoruz
            genel.frame_kontrol_baslangic_zamani = datetime.datetime.now().strftime('%-d %b %Y %a  %-H:%M:%S')
            # eğer başlangıç anı ile bitiş anı zamanları aynı değilse yani zaman 1 saniye ilerlemişse
            if genel.frame_kontrol_baslangic_zamani != genel.frame_kontrol_bitis_zamani:
                genel.gerceklesen_frame_sayisi = genel.saniyede_gerceklesen_frame_sayisi
                genel.frame_kontrol_bitis_zamani = datetime.datetime.now().strftime('%-d %b %Y %a  %-H:%M:%S')
                genel.saniyede_gerceklesen_frame_sayisi = 0

        neo_car_gui.update_idletasks()

        genel.kontrol_cevrimi_after_id = msg_lbl.after(1, genel.kontrol_cevrimi)



class acilis():
    def __init__(self):

        os.chdir('/home/pi/Desktop/Neo_Car_Sign_Detection/')

        # klavyeden yaptığımız kontrollerde tuşların release zamanlarını tutup mükerrer release işlemini engellemek için bu dict'i yapıyoruz        
        genel.kontrol_tuslari_birakma_zamanlari = {"q": datetime.datetime(2100, 1, 1, 0, 0), \
                                                   "w": datetime.datetime(2100, 1, 1, 0, 0), \
                                                   "Up": datetime.datetime(2100, 1, 1, 0, 0), \
                                                   "e": datetime.datetime(2100, 1, 1, 0, 0), \
                                                   "a": datetime.datetime(2100, 1, 1, 0, 0), \
                                                   "Left": datetime.datetime(2100, 1, 1, 0, 0), \
                                                   "s-space": datetime.datetime(2100, 1, 1, 0, 0), \
                                                   "d": datetime.datetime(2100, 1, 1, 0, 0), \
                                                   "Right": datetime.datetime(2100, 1, 1, 0, 0), \
                                                   "z": datetime.datetime(2100, 1, 1, 0, 0), \
                                                   "x": datetime.datetime(2100, 1, 1, 0, 0), \
                                                   "Down": datetime.datetime(2100, 1, 1, 0, 0), \
                                                   "c": datetime.datetime(2100, 1, 1, 0, 0)}
        #print("\ngenel.kontrol_tuslari_birakma_zamanlari :", genel.kontrol_tuslari_birakma_zamanlari)
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(0)
        GPIO.cleanup()

        # Led kontrol pinleri
        GPIO.setup(genel.on_alt_kisa_beyaz_stop_lambalar_kontrol_pini, GPIO.OUT, initial=0)
        GPIO.setup(genel.on_ust_uzun_beyaz_farlar_kontrol_pini, GPIO.OUT, initial=0)
        GPIO.setup(genel.on_sol_sari_sinyal_fari_kontrol_pini, GPIO.OUT, initial=0)
        GPIO.setup(genel.on_sag_sari_sinyal_fari_kontrol_pini, GPIO.OUT, initial=0)
        GPIO.setup(genel.arka_sol_sari_sinyal_fari_kontrol_pini, GPIO.OUT, initial=0)
        GPIO.setup(genel.arka_sag_sari_sinyal_fari_kontrol_pini, GPIO.OUT, initial=0)
        GPIO.setup(genel.arka_alt_kirmizi_kisa_stop_lambalar_kontrol_pini, GPIO.OUT, initial=0)
        GPIO.setup(genel.arka_orta_kirmizi_parlak_fren_lambalari_kontrol_pini, GPIO.OUT, initial=0)
        GPIO.setup(genel.arka_ust_tek_beyaz_geri_vites_lambasi_kontrol_pini, GPIO.OUT, initial=0)

        msg_lbl['text'] = "AÇILIŞ - Led pinleri ayarlandı - OK"
        time.sleep(0.5)
        neo_car_gui.update_idletasks()    

        # motor pinleri
        GPIO.setup(genel.sag_motorlar_one_hareket_pini, GPIO.OUT, initial=0)
        GPIO.setup(genel.sag_motorlar_arkaya_hareket_pini, GPIO.OUT, initial=0)    
        GPIO.setup(genel.sol_motorlar_one_hareket_pini, GPIO.OUT, initial=0)
        GPIO.setup(genel.sol_motorlar_arkaya_hareket_pini, GPIO.OUT, initial=0)
        GPIO.setup(genel.sag_motorlar_pwm_pini, GPIO.OUT, initial=0)
        GPIO.setup(genel.sol_motorlar_pwm_pini, GPIO.OUT, initial=0)
        genel.sag_motorlar_pwm = GPIO.PWM(genel.sag_motorlar_pwm_pini, 100)
        genel.sag_motorlar_pwm.start(0)
        genel.sol_motorlar_pwm = GPIO.PWM(genel.sol_motorlar_pwm_pini, 100)
        genel.sol_motorlar_pwm.start(0)
        msg_lbl['text'] = "AÇILIŞ - Motor pinleri ayarlandı - OK"
        time.sleep(0.5)
        neo_car_gui.update_idletasks()

        # Mesafe Sensörleri TRIG pinleri Multiplexer'a takılı, Multiplexer kontrol pinleri
        GPIO.setup(genel.multiplexer_SO_kontrol_pini, GPIO.OUT, initial=0)
        GPIO.setup(genel.multiplexer_S1_kontrol_pini, GPIO.OUT, initial=0)
        GPIO.setup(genel.multiplexer_S2_kontrol_pini, GPIO.OUT, initial=0)
        GPIO.setup(genel.multiplexer_S3_kontrol_pini, GPIO.OUT, initial=0)
        GPIO.setup(genel.multiplexer_SIG_kontrol_pini, GPIO.OUT, initial=0)
        # mesafe sensörleri Echo pinleri (Trig pinleri multiplexer üzerinde)
        GPIO.setup(genel.on_orta_mesafe_sensoru_echo_pini, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(genel.on_sag_mesafe_sensoru_echo_pini, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(genel.on_sol_mesafe_sensoru_echo_pini, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(genel.sag_mesafe_sensoru_echo_pini, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(genel.sol_mesafe_sensoru_echo_pini, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(genel.arka_orta_mesafe_sensoru_echo_pini, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(genel.arka_sag_mesafe_sensoru_echo_pini, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(genel.arka_sol_mesafe_sensoru_echo_pini, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        msg_lbl['text'] = "AÇILIŞ - Mesafe sensörü pinleri ayarlandı - OK"
        time.sleep(0.5)
        neo_car_gui.update_idletasks()    

        # 8 sensörü çalıştırıp aracın etrafındaki nesnelerle arasındaki mesafeleri ölçen thread, 0.5 saniyede bir güncelliyor
        mesafe_olcumu_thread = threading.Thread(target=genel.otomatik_mesafe_olcum)
        genel.otomatik_mesafe_olcum_thread_calissin_mi = True
        mesafe_olcumu_thread.start()
        msg_lbl['text'] = "AÇILIŞ - Mesafe sensör thread'i çalıştırıldı - OK"
        neo_car_gui.update_idletasks()
        time.sleep(0.5)

        # 4 sinyal lambasını sol - sağ - dörtlü sinyalleri aracın hareketinden bağımsız çalıştırmak için oluşturulan thread
        sinyal_calistirma_thread = threading.Thread(target=genel.sinyal_thread)
        genel.sinyal_thread_calissin_mi = True
        sinyal_calistirma_thread.start()
        msg_lbl['text'] = "AÇILIŞ - Sinyal thread'i çalıştırıldı - OK"
        neo_car_gui.update_idletasks()
        time.sleep(0.5)

        # Klavyeden basılan tuşların durumlarını kontrol ederek motorları kontrol ediyoruz
        klavyeden_motor_kontrol_thread = threading.Thread(target=genel.tuslarin_durumu_ile_motor_kontrol)
        genel.klavyeden_motor_kontrol_thread_calissin_mi = True
        klavyeden_motor_kontrol_thread.start()
        msg_lbl['text'] = "AÇILIŞ - Klavyeden motor kontrol thread'i çalıştırıldı - OK"
        neo_car_gui.update_idletasks()
        time.sleep(0.5)

        # Kamera görüntü ayarlarını yapıyoruz
        genel.video = cv2.VideoCapture(0)
        genel.video.set(3, genel.frameWidth)
        genel.video.set(4, genel.frameHeight)
        genel.video.set(cv2.CAP_PROP_FPS, genel.set_edilen_Fps)
        genel.video.set(10, 180)        #brightness
        genel.detection_threshold = 0.75

        # saniyede gerçekleşen frame sayısını ölçmek için bu değişkenleri kontrol_cevrimi fonksiyonu içinde kullanacağız
        genel.frame_kontrol_baslangic_zamani    = datetime.datetime.now().strftime('%-d %b %Y %a  %-H:%M:%S')
        genel.frame_kontrol_bitis_zamani        = datetime.datetime.now().strftime('%-d %b %Y %a  %-H:%M:%S')
        genel.saniyede_gerceklesen_frame_sayisi = 0
        msg_lbl['text'] = "AÇILIŞ - Kamera parametreleri ayarlandı - OK"
        neo_car_gui.update_idletasks()
        time.sleep(0.5)        

        genel.selektor_yap()
        time.sleep(0.2)
        genel.kisa_far_kontrolu()

        msg_lbl['text'] = "Açılış - OK"
        neo_car_gui.update_idletasks()

        genel.kontrol_cevrimi()


if __name__ == "__main__":

    from tkinter import *    
    neo_car_gui = Tk()
    menu_genisligi = 1000 ; menu_yuksekligi = 600 ; uste_yakinlik = 50
    neo_car_gui.geometry("%dx%d+%d+%d" %(menu_genisligi, menu_yuksekligi, ((neo_car_gui.winfo_screenwidth() / 2) - \
            (menu_genisligi / 2)), (((neo_car_gui.winfo_screenheight() / 2) - (menu_yuksekligi / 2)) - uste_yakinlik)))
    neo_car_gui.resizable(0, 0)
    neo_car_gui.title("Neo Car Control Panel")
    neo_car_gui['bg'] = "gray92"
    neo_car_gui.protocol("WM_DELETE_WINDOW", genel.programi_sonlandir)

    widget_list = []
    widget_list.append(neo_car_gui)
 
    msg_lbl = Label(neo_car_gui, text="Kütüphaneler yükleniyor...", font="Arial 12", bg="white", pady=5)
    msg_lbl.place(x=int(menu_genisligi*0.05), y=int(menu_yuksekligi*0.71), width=(menu_genisligi*0.9))
    widget_list.append(msg_lbl)
    
    neo_car_gui.update_idletasks()

    import os
    import sys
    import cv2
    import time    
    import datetime
    import threading
    import tensorflow
    import numpy as np
    import RPi.GPIO as GPIO
    from tensorflow import keras    
    from PIL import ImageTk, Image
    from tensorflow.keras.preprocessing import image
    model = tensorflow.keras.models.load_model('best_model3.h5')

    mesafe_lbl = Label(neo_car_gui, text="", font="Arial 12", bg="white", pady=5)
    mesafe_lbl.place(x=int(menu_genisligi*0.05), y=int(menu_yuksekligi*0.78), width=(menu_genisligi*0.9))

    far_lbl = Label(neo_car_gui, text="", font="Arial 12", bg="white", pady=5)
    far_lbl.place(x=int(menu_genisligi*0.05), y=int(menu_yuksekligi*0.85), width=(menu_genisligi*0.9))

    sinyal_lbl = Label(neo_car_gui, text="", font="Arial 12", bg="white", pady=5)
    sinyal_lbl.place(x=int(menu_genisligi*0.05), y=int(menu_yuksekligi*0.92), width=(menu_genisligi*0.9))

    goruntu_lbl = Label(neo_car_gui, bg="blue")
    goruntu_lbl.place(x=int(menu_genisligi*0.42), y=int(menu_yuksekligi*0.05), width=genel.frameWidth+2, height=genel.frameHeight+2)

    # Yön butonları
    ok_btn_x          = int(menu_genisligi*0.2)
    ok_btn_y          = int(menu_yuksekligi*0.07)
    ok_btn_genislik   = 46
    ok_btn_yukseklik  = 46
    ok_btn_ara_mesafe = 6

    yukari_ok_img = ImageTk.PhotoImage(Image.open("yukari_ok_32x32.png"))
    yukari_btn = Button (neo_car_gui, width=ok_btn_genislik, height=ok_btn_yukseklik, image=yukari_ok_img, bd=1, command=genel.arac_duz_ileri_gidiyor)
    yukari_btn.place(x=ok_btn_x, y=ok_btn_y)
    widget_list.append(yukari_btn)

    sag_ust_ok_img = ImageTk.PhotoImage(Image.open("sag_ust_ok_32x32.png"))
    sag_ust_ok_btn = Button (neo_car_gui, width=ok_btn_genislik, height=ok_btn_yukseklik, image=sag_ust_ok_img, bd=1, command=genel.arac_ileri_saga_donuyor)
    sag_ust_ok_btn.place(x=ok_btn_x + ok_btn_genislik + ok_btn_ara_mesafe, y = ok_btn_y + ok_btn_ara_mesafe + int(ok_btn_yukseklik / 2))
    widget_list.append(sag_ust_ok_btn)

    sag_ok_img = ImageTk.PhotoImage(Image.open("sag_ok_32x32.png"))
    sag_ok_btn = Button (neo_car_gui, width=ok_btn_genislik, height=ok_btn_yukseklik, image=sag_ok_img, bd=1, command=genel.arac_tam_saga_donuyor)
    sag_ok_btn.place(x=ok_btn_x + int((1.5 * ok_btn_genislik) + (2 * ok_btn_ara_mesafe)), y = ok_btn_y + (2 * ok_btn_ara_mesafe) + (ok_btn_yukseklik * 1.5))
    widget_list.append(sag_ok_btn)

    sag_alt_ok_img = ImageTk.PhotoImage(Image.open("sag_alt_ok_32x32.png"))
    sag_alt_ok_btn = Button (neo_car_gui, width=ok_btn_genislik, height=ok_btn_yukseklik, image=sag_alt_ok_img, bd=1, command=genel.arac_geri_saga_donuyor)
    sag_alt_ok_btn.place(x=ok_btn_x + ok_btn_genislik + ok_btn_ara_mesafe, y = ok_btn_y + (3 * ok_btn_ara_mesafe) + (2.5 * ok_btn_yukseklik))
    widget_list.append(sag_alt_ok_btn)

    asagi_ok_img = ImageTk.PhotoImage(Image.open("asagi_ok_32x32.png"))
    asagi_btn = Button (neo_car_gui, width=ok_btn_genislik, height=ok_btn_yukseklik, image=asagi_ok_img, bd=1, command=genel.arac_duz_geri_gidiyor)
    asagi_btn.place(x=ok_btn_x, y=ok_btn_y + (4 * ok_btn_ara_mesafe) + (3 * ok_btn_yukseklik))
    widget_list.append(asagi_btn)

    sol_ust_ok_img = ImageTk.PhotoImage(Image.open("sol_ust_ok_32x32.png"))
    sol_ust_ok_btn = Button (neo_car_gui, width=ok_btn_genislik, height=ok_btn_yukseklik, image=sol_ust_ok_img, bd=1, command=genel.arac_ileri_sola_donuyor)
    sol_ust_ok_btn.place(x=ok_btn_x - ok_btn_genislik - ok_btn_ara_mesafe, y = ok_btn_y + ok_btn_ara_mesafe + int(ok_btn_yukseklik / 2))
    widget_list.append(sol_ust_ok_btn)

    sol_ok_img = ImageTk.PhotoImage(Image.open("sol_ok_32x32.png"))
    sol_ok_btn = Button (neo_car_gui, width=ok_btn_genislik, height=ok_btn_yukseklik, image=sol_ok_img, bd=1, command=genel.arac_tam_sola_donuyor)
    sol_ok_btn.place(x=ok_btn_x - int((2 * ok_btn_genislik) - (2 * ok_btn_ara_mesafe)), y = ok_btn_y + (2 * ok_btn_ara_mesafe) + (ok_btn_yukseklik * 1.5))
    widget_list.append(sol_ok_btn)

    sol_alt_ok_img = ImageTk.PhotoImage(Image.open("sol_alt_ok_32x32.png"))
    sol_alt_ok_btn = Button (neo_car_gui, width=ok_btn_genislik, height=ok_btn_yukseklik, image=sol_alt_ok_img, bd=1, command=genel.arac_geri_sola_donuyor)
    sol_alt_ok_btn.place(x=ok_btn_x - ok_btn_genislik - ok_btn_ara_mesafe, y = ok_btn_y + (3 * ok_btn_ara_mesafe) + (2.5 * ok_btn_yukseklik))
    widget_list.append(sol_alt_ok_btn)

    stop_img = ImageTk.PhotoImage(Image.open("stop_btn_40x40.png"))
    stop_btn = Button (neo_car_gui, width=ok_btn_genislik, height=ok_btn_yukseklik, image=stop_img, bd=1, command=genel.arac_durdu)
    stop_btn.place(x=ok_btn_x, y = ok_btn_y + (2 * ok_btn_ara_mesafe) + (ok_btn_yukseklik * 1.5))
    widget_list.append(stop_btn)

    kisalar_img = ImageTk.PhotoImage(Image.open("kisalar_44x44.png"))
    kisalar_btn = Button (neo_car_gui, width=ok_btn_genislik, height=ok_btn_yukseklik, image=kisalar_img, bd=1, command=genel.kisa_far_kontrolu)
    kisalar_btn.place(x=ok_btn_x - int((2 * ok_btn_genislik) - (2 * ok_btn_ara_mesafe)), y=ok_btn_y + (5 * ok_btn_ara_mesafe) + (4.5* ok_btn_yukseklik))
    widget_list.append(kisalar_btn)

    uzunlar_img = ImageTk.PhotoImage(Image.open("uzunlar_44x44.png"))
    uzunlar_btn = Button (neo_car_gui, width=ok_btn_genislik, height=ok_btn_yukseklik, image=uzunlar_img, bd=1, command=genel.uzun_far_kontrolu)
    uzunlar_btn.place(x=ok_btn_x, y=ok_btn_y + (5 * ok_btn_ara_mesafe) + (4.5 * ok_btn_yukseklik))
    widget_list.append(uzunlar_btn)

    selektor_img = ImageTk.PhotoImage(Image.open("selektor_44x44.png"))
    selektor_btn = Button (neo_car_gui, width=ok_btn_genislik, height=ok_btn_yukseklik, image=selektor_img, bd=1, command=genel.selektor_yap)
    selektor_btn.place(x=ok_btn_x + int((1.5 * ok_btn_genislik) + (2 * ok_btn_ara_mesafe)), y=ok_btn_y + (5 * ok_btn_ara_mesafe) + (4.5 * ok_btn_yukseklik))
    widget_list.append(selektor_btn)

    disco_mode_img = ImageTk.PhotoImage(Image.open("disco_44x30.png"))
    disco_mode_btn = Button (neo_car_gui, width=ok_btn_genislik, height=ok_btn_yukseklik, image=disco_mode_img, bd=1, command=genel.disco_mode_kontrolu)
    disco_mode_btn.place(x=ok_btn_x, y=ok_btn_y + (7 * ok_btn_ara_mesafe) + (5.5 * ok_btn_yukseklik))
    widget_list.append(disco_mode_btn)

    dortluler_img = ImageTk.PhotoImage(Image.open("dortlu_sinyal_36x35.png"))
    dortluler_btn = Button (neo_car_gui, width=ok_btn_genislik, height=ok_btn_yukseklik, image=dortluler_img, bd=1, command=genel.dortlu_sinyal_kontrolu)
    dortluler_btn.place(x=ok_btn_x + int((1.5 * ok_btn_genislik) + (2 * ok_btn_ara_mesafe)), y=ok_btn_y + (7 * ok_btn_ara_mesafe) + (5.5 * ok_btn_yukseklik))
    widget_list.append(dortluler_btn)

    for widget in widget_list:
        widget.bind("<Escape>", genel.programi_sonlandir)
        widget.bind("<KeyPress>", genel.tus_basma_kontrol)
        widget.bind("<KeyRelease>", genel.tus_birakma_zaman_takip)

    del menu_genisligi, menu_yuksekligi, uste_yakinlik, ok_btn_x, ok_btn_y, ok_btn_genislik, ok_btn_yukseklik, ok_btn_ara_mesafe

    neo_car_gui.update_idletasks()

    acilis()

    neo_car_gui.mainloop()
        
