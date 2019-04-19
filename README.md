# 32x16dz
二塊 16x16 點陣跑馬燈的應用，供趨勢魅客社2019年5月教學使用。

晶片: 74HC138, 74HC595

# 準備材料
1. 74HC138 + 74HC595 的 16x16 點陣LED顯示器 ... 2 塊
1. Arduino Nano ... 1 片
1. 焊接工具

# 步驟
1. 將第一塊 16x16點陣顯示器 的 CN2-out 焊上排針
1. 將第一塊 16x16點陣顯示器 的 CN3 焊上排針
1. 用 jumper 把兩塊點陣顯示器連接起來
1. 用杜邦線把 Arduino Nano 和 16x16點陣顯示器 接起來。參考接腳如下

| Arduino | 點陣顯示器 |
| +5V	| +5V |
| GND	| GND |
| D5	| A |
| D4	| B |
| D3	| C |
| D2	| D |
| D6	| G |
| D7	| DI |
| D8	| CLK |
| D9	| ALT |

# 中文字型
據說倚天中文字型必須取得授權才能使用，國喬字型檔只要非商業使用，就可以免授權。但是在 [MIT 的這個 FTP 站]
 (https://lost-contact.mit.edu/afs//ir.stanford.edu/systems/hp_ux110/pubsw/lib/hbf/big5/) 可以下載到所有古時候的中文字型。
請大家自己斟酌使用。

# License
我自己寫的程式全部都以 MIT license 釋出。
