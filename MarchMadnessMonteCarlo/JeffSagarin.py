#!/usr/bin/env python
from . import config

if config.date == 2023:
    lineparts = ["Rank","Team","Rating","W","L","Schedule","ScheduleRank","WinsVsTop25","LossesVsTop25","WinsVsTop50","LossesVsTop50",
                 "PREDICTOR","PREDICTOR_RANK",
                 "GOLDENMEAN_SCORE","GOLDENMEAN_RANK",
                 "RECENT","RECENT_RANK","CONFERENCE"]
    text = """
      RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
   1  Houston                 =  92.47   29   2   75.55(  93)    1   1  |    5   1  |   93.07    1 |   93.11    1 |   91.86    1  AMER. ATHLETIC
   2  UCLA                    =  90.96   28   4   78.77(  46)    3   2  |    6   4  |   90.72    4 |   91.14    2 |   90.90    3  PAC-12
   3  Gonzaga                 =  90.48   27   5   77.48(  70)    6   4  |    6   4  |   89.95    6 |   91.10    3 |   90.37    4  WEST COAST
   4  Alabama                 =  90.47   26   5   80.98(  13)    5   4  |   11   4  |   91.02    3 |   90.75    5 |   90.01    6  SOUTHEASTERN
   5  Connecticut             =  90.47   25   7   79.30(  38)    3   4  |   10   5  |   90.27    5 |   89.61    7 |   90.99    2  BIG EAST
   6  Kansas                  =  90.29   26   6   83.01(   1)   10   5  |   16   6  |   89.61    7 |   91.08    4 |   90.21    5  BIG 12
   7  Tennessee               =  90.02   23   9   79.34(  36)    5   4  |    9   5  |   91.34    2 |   89.14    9 |   89.86    7  SOUTHEASTERN
   8  Texas                   =  89.48   24   8   81.52(   9)    8   5  |   13   8  |   89.57    8 |   89.49    8 |   89.33    8  BIG 12
   9  Arizona                 =  89.05   26   6   78.48(  52)    4   1  |    8   2  |   89.19    9 |   88.64   10 |   89.09   10  PAC-12
  10  Purdue                  =  88.86   26   5   80.62(  17)    7   3  |   14   5  |   88.81   10 |   90.10    6 |   88.29   11  BIG TEN
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
  11  Creighton               =  88.43   21  11   80.51(  19)    3   6  |    7   8  |   88.38   11 |   87.23   14 |   89.10    9  BIG EAST
  12  Baylor                  =  87.35   22  10   82.28(   5)    8   6  |   12  10  |   88.28   12 |   88.55   11 |   86.41   16  BIG 12
  13  Duke                    =  86.63   24   8   78.55(  51)    1   2  |    7   6  |   85.95   21 |   86.69   16 |   86.87   13  ATLANTIC COAST
  14  Kentucky                =  86.57   21  10   79.29(  40)    4   6  |    7   6  |   85.97   20 |   86.45   19 |   86.86   14  SOUTHEASTERN
  15  Marquette               =  86.50   26   6   79.23(  41)    5   3  |    8   5  |   86.32   17 |   87.50   12 |   86.05   18  BIG EAST
  16  Saint Mary's-Cal.       =  86.44   25   7   76.76(  77)    1   3  |    2   3  |   87.51   13 |   87.18   15 |   85.59   24  WEST COAST
  17  Xavier-Ohio             =  86.34   24   8   79.84(  28)    5   5  |    8   6  |   85.97   19 |   87.34   13 |   85.99   19  BIG EAST
  18  TCU                     =  86.16   21  11   80.55(  18)    6   5  |   11   9  |   86.44   15 |   86.45   18 |   85.79   22  BIG 12
  19  Indiana                 =  86.11   21  10   81.00(  12)    4   4  |   11  10  |   86.54   14 |   86.51   17 |   85.63   23  BIG TEN
  20  Maryland                =  86.04   21  11   79.50(  33)    2   4  |    8   9  |   85.59   25 |   85.26   30 |   86.66   15  BIG TEN
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
  21  Arkansas                =  86.04   20  12   79.73(  31)    2   7  |    4   9  |   86.42   16 |   85.72   22 |   85.92   20  SOUTHEASTERN
  22  Texas A&M               =  85.88   23   8   77.68(  67)    3   2  |    5   4  |   85.09   30 |   84.67   32 |   87.03   12  SOUTHEASTERN
  23  West Virginia           =  85.84   19  14   82.37(   4)    2  11  |    8  13  |   85.60   23 |   85.42   27 |   86.09   17  BIG 12
  24  Michigan State          =  85.66   19  11   82.12(   6)    3   5  |   11  10  |   84.99   31 |   85.70   23 |   85.90   21  BIG TEN
  25  Kansas State            =  85.35   23   9   80.44(  21)    6   5  |   10   7  |   85.24   29 |   85.41   28 |   85.27   25  BIG 12
  26  Iowa State              =  85.32   19  12   82.54(   2)    8   6  |   11  10  |   85.94   22 |   85.48   25 |   84.87   27  BIG 12
  27  Illinois                =  85.29   20  12   79.81(  29)    3   4  |    7  11  |   85.99   18 |   85.38   29 |   84.85   28  BIG TEN
  28  Auburn                  =  85.23   20  12   79.99(  26)    2   8  |    4  10  |   85.38   27 |   85.05   31 |   85.15   26  SOUTHEASTERN
  29  Iowa                    =  84.90   19  13   80.78(  14)    4   4  |   12   8  |   85.44   26 |   84.66   33 |   84.68   30  BIG TEN
  30  Virginia                =  84.83   24   6   77.96(  61)    2   1  |    8   3  |   84.79   32 |   86.30   20 |   84.14   36  ATLANTIC COAST
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
  31  Memphis                 =  84.78   23   8   77.96(  60)    1   3  |    2   3  |   84.38   34 |   85.59   24 |   84.51   33  AMER. ATHLETIC
  32  Miami-Florida           =  84.57   25   6   77.37(  72)    1   2  |    7   3  |   83.68   44 |   85.46   26 |   84.53   32  ATLANTIC COAST
  33  San Diego State         =  84.32   24   6   77.31(  73)    0   3  |    3   3  |   85.25   28 |   86.20   21 |   83.12   49  MOUNTAIN WEST
  34  Michigan                =  84.29   17  15   80.76(  15)    2   6  |    7  12  |   83.74   40 |   84.37   35 |   84.44   34  BIG TEN
  35  North Carolina          =  84.26   20  13   79.33(  37)    0   4  |    5   9  |   84.46   33 |   84.51   34 |   83.95   39  ATLANTIC COAST
  36  Southern California     =  84.17   22  10   78.19(  58)    1   4  |    2   5  |   84.08   39 |   84.32   36 |   84.06   37  PAC-12
  37  Providence              =  84.17   21  11   78.33(  53)    3   7  |    5   8  |   84.10   37 |   84.04   38 |   84.17   35  BIG EAST
  38  Northwestern            =  84.15   21  10   79.68(  32)    4   1  |    8   9  |   83.73   42 |   83.51   42 |   84.64   31  BIG TEN
  39  Rutgers                 =  84.15   19  13   79.36(  35)    4   2  |    9   9  |   85.59   24 |   83.63   41 |   83.71   41  BIG TEN
  40  Utah State              =  83.90   24   7   76.05(  87)    0   0  |    0   2  |   84.11   36 |   84.02   39 |   83.65   42  MOUNTAIN WEST
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
  41  Oregon                  =  83.74   19  13   79.22(  42)    1   6  |    3   6  |   83.72   43 |   83.26   44 |   83.90   40  PAC-12
  42  Clemson                 =  83.60   23   9   76.06(  86)    1   0  |    5   4  |   82.46   52 |   82.55   53 |   84.83   29  ATLANTIC COAST
  43  Texas Tech              =  83.56   16  16   80.23(  23)    3  11  |    4  15  |   84.22   35 |   83.03   48 |   83.43   44  BIG 12
  44  Oklahoma State          =  83.48   18  15   81.83(   7)    2  12  |    6  12  |   84.08   38 |   83.87   40 |   82.92   51  BIG 12
  45  NC State                =  83.29   23  10   77.82(  66)    1   2  |    3   8  |   83.17   46 |   83.08   46 |   83.36   45  ATLANTIC COAST
  46  Villanova               =  83.27   17  16   80.25(  22)    2   8  |    2  12  |   82.79   49 |   82.33   54 |   83.97   38  BIG EAST
  47  Florida Atlantic        =  83.18   27   3   72.16( 145)    0   0  |    0   0  |   83.06   47 |   82.81   49 |   83.34   47  CONFERENCE USA
  48  Penn State              =  83.06   20  12   80.05(  25)    2   4  |    9   8  |   82.55   51 |   83.34   43 |   83.09   50  BIG TEN
  49  Ohio State              =  82.90   15  18   81.47(  10)    1   7  |    7  15  |   83.74   41 |   82.79   50 |   82.49   52  BIG TEN
  50  Mississippi State       =  82.82   21  11   77.93(  62)    4   5  |    4   6  |   83.05   48 |   83.24   45 |   82.42   53  SOUTHEASTERN
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
  51  Cincinnati              =  82.62   19  11   75.24(  98)    0   4  |    0   7  |   82.78   50 |   81.23   63 |   83.26   48  AMER. ATHLETIC
  52  Boise State             =  82.36   23   8   76.48(  82)    1   0  |    3   2  |   83.59   45 |   84.10   37 |   81.06   66  MOUNTAIN WEST
  53  VCU(Va. Commonwealth)   =  82.33   25   7   73.22( 119)    0   0  |    0   1  |   81.09   63 |   81.47   59 |   83.48   43  ATLANTIC 10
  54  Oklahoma                =  81.98   15  17   82.53(   3)    4  10  |    6  16  |   82.14   55 |   82.69   51 |   81.48   61  BIG 12
  55  UAB                     =  81.90   23   8   71.84( 155)    0   1  |    1   2  |   81.80   57 |   81.46   60 |   82.08   55  CONFERENCE USA
  56  Drake                   =  81.88   26   7   72.22( 139)    0   0  |    1   0  |   80.14   76 |   81.06   64 |   83.35   46  MISSOURI VALLEY
  57  Wisconsin               =  81.65   17  14   81.54(   8)    2   5  |    9  12  |   81.86   56 |   82.61   52 |   81.02   68  BIG TEN
  58  Missouri                =  81.61   23   8   77.88(  64)    3   5  |    6   7  |   81.68   58 |   83.07   47 |   80.85   72  SOUTHEASTERN
  59  North Texas             =  81.61   24   6   72.81( 124)    0   1  |    0   3  |   80.94   69 |   81.26   61 |   82.06   56  CONFERENCE USA
  60  Arizona State           =  81.59   22  11   78.68(  47)    2   3  |    5   6  |   81.64   59 |   82.31   55 |   81.14   65  PAC-12
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
  61  Pittsburgh              =  81.58   22  11   77.20(  74)    0   3  |    6   6  |   81.00   66 |   80.88   66 |   82.18   54  ATLANTIC COAST
  62  Seton Hall              =  81.49   16  15   80.20(  24)    1   8  |    4  12  |   82.14   54 |   81.61   56 |   81.03   67  BIG EAST
  63  Florida                 =  81.40   16  16   79.78(  30)    1  10  |    2  13  |   82.42   53 |   81.61   57 |   80.74   73  SOUTHEASTERN
  64  Colorado                =  81.18   17  16   78.60(  48)    2   4  |    3   7  |   81.45   60 |   81.23   62 |   80.93   71  PAC-12
  65  Dayton                  =  81.08   21  11   73.16( 121)    0   0  |    0   1  |   80.94   68 |   80.56   68 |   81.34   62  ATLANTIC 10
  66  Washington State        =  81.02   17  16   78.96(  43)    1   4  |    3   8  |   81.07   64 |   80.39   71 |   81.22   64  PAC-12
  67  Vanderbilt              =  81.01   19  13   79.29(  39)    3   6  |    5   8  |   79.74   79 |   80.32   72 |   82.04   57  SOUTHEASTERN
  68  BYU                     =  80.88   17  15   75.74(  89)    1   5  |    1   7  |   80.88   70 |   79.99   75 |   81.27   63  WEST COAST
  69  Toledo                  =  80.76   25   6   70.17( 224)    0   0  |    0   0  |   80.25   75 |   79.76   79 |   81.50   60  MAC
  70  Virginia Tech           =  80.71   19  14   77.67(  68)    1   1  |    5   8  |   81.13   62 |   80.89   65 |   80.32   76  ATLANTIC COAST
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
  71  Central Florida(UCF)    =  80.70   18  13   75.55(  94)    0   2  |    2   4  |   81.43   61 |   79.83   78 |   80.73   74  AMER. ATHLETIC
  72  College of Charleston   =  80.68   30   3   68.96( 274)    0   0  |    0   1  |   79.09   85 |   79.95   76 |   81.93   58  COLONIAL
  73  Stanford                =  80.63   14  19   78.56(  50)    1   4  |    2   8  |   80.39   73 |   78.72   87 |   81.81   59  PAC-12
  74  St. John's              =  80.61   18  15   78.24(  56)    1   8  |    2  12  |   79.87   77 |   80.46   69 |   80.98   70  BIG EAST
  75  Oral Roberts            =  80.49   26   4   68.83( 277)    0   2  |    0   3  |   80.94   67 |   81.48   58 |   79.74   81  SUMMIT LEAGUE
  76  Yale                    =  80.19   18   7   71.34( 174)    0   1  |    0   1  |   79.81   78 |   78.94   85 |   81.01   69  IVY LEAGUE
  77  Kent State              =  80.04   24   6   71.18( 178)    0   2  |    0   2  |   80.44   72 |   80.44   70 |   79.55   83  MAC
  78  Wake Forest             =  79.78   19  14   77.62(  69)    1   1  |    3   9  |   79.25   83 |   80.01   74 |   79.84   79  ATLANTIC COAST
  79  Furman                  =  79.47   24   7   70.14( 226)    0   0  |    0   2  |   78.33   89 |   78.77   86 |   80.40   75  SOUTHERN
  80  Bradley                 =  79.43   24   9   72.57( 133)    0   1  |    0   3  |   79.26   82 |   79.17   82 |   79.55   82  MISSOURI VALLEY
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
  81  Iona                    =  79.40   25   7   69.76( 241)    0   0  |    0   0  |   79.33   81 |   78.28   89 |   79.95   78  METRO ATLANTIC
  82  Utah                    =  79.39   17  15   77.87(  65)    1   4  |    1   9  |   81.00   65 |   79.69   80 |   78.44   87  PAC-12
  83  Santa Clara             =  79.36   22   9   74.75( 102)    0   4  |    0   5  |   79.23   84 |   80.16   73 |   78.95   86  WEST COAST
  84  Saint Louis             =  79.22   20  11   74.93( 101)    0   1  |    2   2  |   78.68   86 |   79.40   81 |   79.32   84  ATLANTIC 10
  85  Nevada                  =  79.20   21  10   76.50(  80)    0   1  |    2   4  |   80.35   74 |   80.69   67 |   77.95   94  MOUNTAIN WEST
  86  New Mexico              =  79.12   21  11   75.24(  97)    1   0  |    2   3  |   80.72   71 |   79.95   77 |   77.96   93  MOUNTAIN WEST
  87  Liberty                 =  78.92   23   8   69.05( 271)    0   1  |    0   2  |   79.62   80 |   79.15   83 |   78.38   88  ATLANTIC SUN
  88  Hofstra                 =  78.89   23   9   70.42( 211)    0   2  |    0   2  |   77.86   92 |   77.29   99 |   80.30   77  COLONIAL
  89  Nebraska                =  78.35   16  16   81.21(  11)    2   7  |    7  13  |   77.57  100 |   79.07   84 |   78.30   89  BIG TEN
  90  Indiana State           =  78.25   21  12   70.09( 230)    0   0  |    0   0  |   77.78   93 |   75.95  110 |   79.77   80  MISSOURI VALLEY
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
  91  Sam Houston State       =  78.24   21   6   72.17( 144)    0   0  |    0   1  |   78.50   87 |   78.36   88 |   77.96   92  WESTERN ATHLETIC
  92  Wichita State           =  78.24   17  14   74.57( 103)    0   3  |    0   6  |   77.60   97 |   77.26  100 |   79.01   85  AMER. ATHLETIC
  93  Utah Valley             =  78.05   22   7   72.09( 148)    0   0  |    1   1  |   77.75   94 |   78.25   90 |   78.00   90  WESTERN ATHLETIC
  94  San Francisco           =  77.95   19  14   75.16(  99)    0   5  |    0   6  |   78.25   90 |   78.23   91 |   77.58   97  WEST COAST
  95  Syracuse                =  77.93   17  15   76.48(  83)    0   1  |    1   7  |   77.64   96 |   77.95   94 |   77.96   91  ATLANTIC COAST
  96  Marshall                =  77.64   23   8   70.12( 229)    0   0  |    0   0  |   78.48   88 |   78.11   92 |   76.93  104  SUN BELT
  97  Tulane                  =  77.56   19  10   73.65( 112)    0   2  |    2   2  |   77.46  101 |   78.09   93 |   77.26  101  AMER. ATHLETIC
  98  Temple                  =  77.55   16  15   76.52(  79)    1   1  |    3   3  |   77.60   99 |   76.83  103 |   77.81   96  AMER. ATHLETIC
  99  Akron                   =  77.54   20  10   71.22( 176)    0   0  |    0   1  |   77.46  102 |   76.90  102 |   77.83   95  MAC
 100  Louisiana               =  77.41   23   7   71.66( 158)    0   1  |    0   1  |   76.62  106 |   77.94   95 |   77.46   99  SUN BELT
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 101  Washington              =  77.22   16  16   78.26(  54)    1   5  |    2   8  |   77.67   95 |   77.52   97 |   76.76  106  PAC-12
 102  Mississippi             =  77.08   12  21   78.78(  45)    0   6  |    1  12  |   77.60   98 |   76.94  101 |   76.79  105  SOUTHEASTERN
 103  UNLV                    =  76.75   18  13   75.44(  96)    0   0  |    0   4  |   77.93   91 |   77.91   96 |   75.56  118  MOUNTAIN WEST
 104  Belmont                 =  76.62   20  11   72.10( 147)    0   0  |    0   0  |   75.66  111 |   75.67  115 |   77.54   98  MISSOURI VALLEY
 105  Vermont                 =  76.28   21  10   69.75( 243)    0   1  |    0   2  |   75.46  117 |   75.24  123 |   77.17  102  AMERICA EAST
 106  South Alabama           =  76.22   17  16   72.19( 141)    0   1  |    0   2  |   75.48  116 |   74.75  125 |   77.31  100  SUN BELT
 107  Colgate                 =  76.14   25   8   67.23( 317)    0   0  |    0   1  |   74.87  123 |   75.64  116 |   76.96  103  PATRIOT
 108  UC Irvine               =  76.11   21  10   70.76( 199)    0   0  |    1   1  |   77.17  103 |   76.78  104 |   75.19  122  BIG WEST
 109  San Jose State          =  76.09   19  12   75.70(  90)    0   1  |    1   3  |   75.79  110 |   75.94  111 |   76.22  110  MOUNTAIN WEST
 110  Butler                  =  76.03   14  18   80.47(  20)    2   8  |    3  13  |   77.14  104 |   77.39   98 |   74.78  125  BIG EAST
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 111  Colorado State          =  76.01   14  18   76.49(  81)    1   0  |    1   6  |   76.56  107 |   76.11  109 |   75.58  117  MOUNTAIN WEST
 112  Davidson                =  75.81   15  16   74.30( 104)    0   1  |    0   1  |   75.49  115 |   75.71  114 |   75.93  113  ATLANTIC 10
 113  UC Santa Barbara        =  75.79   23   7   69.37( 260)    0   0  |    0   0  |   76.10  108 |   76.72  105 |   75.09  123  BIG WEST
 114  Ohio                    =  75.72   18  13   70.62( 206)    0   0  |    0   1  |   75.23  119 |   74.24  136 |   76.67  107  MAC
 115  NC Greensboro           =  75.70   18  12   71.16( 181)    0   1  |    0   2  |   74.96  120 |   75.03  124 |   76.32  109  SOUTHERN
 116  Loyola Marymount        =  75.57   18  12   74.98( 100)    2   2  |    2   3  |   75.81  109 |   76.21  106 |   75.04  124  WEST COAST
 117  James Madison           =  75.47   19  11   70.78( 197)    0   0  |    0   2  |   76.69  105 |   75.73  113 |   74.66  127  SUN BELT
 118  Georgia Tech            =  75.42   13  18   77.40(  71)    0   2  |    1   9  |   74.13  132 |   74.44  131 |   76.53  108  ATLANTIC COAST
 119  Princeton               =  75.39   17   8   70.34( 215)    0   0  |    0   0  |   74.82  126 |   75.45  121 |   75.56  119  IVY LEAGUE
 120  Fordham                 =  75.35   25   7   69.81( 240)    0   1  |    0   1  |   73.93  137 |   75.56  118 |   75.89  114  ATLANTIC 10
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 121  Notre Dame              =  75.19   11  21   76.22(  85)    1   2  |    1   8  |   74.64  127 |   74.12  138 |   75.93  112  ATLANTIC COAST
 122  Pennsylvania            =  75.01   16  12   71.94( 153)    0   1  |    0   2  |   74.09  133 |   74.42  132 |   75.70  116  IVY LEAGUE
 123  DePaul                  =  74.95   10  23   80.67(  16)    1   9  |    2  14  |   74.62  128 |   74.38  134 |   75.30  121  BIG EAST
 124  LSU                     =  74.93   14  19   77.90(  63)    1   8  |    1  11  |   75.49  114 |   76.21  107 |   73.95  137  SOUTHEASTERN
 125  Towson                  =  74.91   21  12   69.62( 250)    0   0  |    0   1  |   73.70  140 |   74.13  137 |   75.84  115  COLONIAL
 126  George Mason            =  74.84   20  13   72.77( 125)    0   0  |    0   1  |   74.84  124 |   75.33  122 |   74.50  130  ATLANTIC 10
 127  Grand Canyon            =  74.79   19  11   71.44( 167)    0   0  |    0   0  |   75.60  112 |   76.11  108 |   73.67  141  WESTERN ATHLETIC
 128  Southern Miss           =  74.77   22   7   70.98( 189)    0   0  |    0   0  |   75.51  113 |   75.88  112 |   73.79  139  SUN BELT
 129  Charlotte               =  74.76   18  14   71.84( 156)    0   0  |    0   2  |   75.28  118 |   74.51  130 |   74.52  129  CONFERENCE USA
 130  Montana State           =  74.75   23   9   70.06( 232)    0   1  |    0   2  |   74.89  122 |   75.58  117 |   74.18  133  BIG SKY
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 131  Southern Illinois       =  74.74   22  10   71.65( 159)    0   0  |    1   0  |   74.40  129 |   75.50  119 |   74.44  132  MISSOURI VALLEY
 132  UMass Lowell            =  74.73   24   7   65.16( 352)    0   0  |    0   1  |   73.46  147 |   73.30  148 |   76.05  111  AMERICA EAST
 133  Boston College          =  74.66   16  17   76.80(  76)    0   2  |    2   8  |   72.90  153 |   74.59  129 |   75.52  120  ATLANTIC COAST
 134  Duquesne                =  74.45   20  12   72.05( 149)    0   1  |    0   1  |   74.33  131 |   74.36  135 |   74.45  131  ATLANTIC 10
 135  Middle Tennessee        =  74.41   17  13   73.96( 106)    0   0  |    1   1  |   74.91  121 |   74.65  127 |   73.95  136  CONFERENCE USA
 136  Missouri State          =  74.34   16  15   72.70( 130)    0   1  |    0   1  |   74.05  134 |   74.02  139 |   74.55  128  MISSOURI VALLEY
 137  Samford                 =  74.28   18  10   70.24( 220)    0   0  |    0   0  |   73.70  141 |   73.87  142 |   74.68  126  SOUTHERN
 138  Southern Utah           =  74.12   17  11   72.66( 131)    0   1  |    0   1  |   74.83  125 |   74.71  126 |   73.39  143  WESTERN ATHLETIC
 139  Fresno State            =  73.76   10  20   75.94(  88)    0   0  |    0   3  |   73.97  135 |   73.12  153 |   73.88  138  MOUNTAIN WEST
 140  Youngstown State        =  73.66   22   9   67.70( 308)    0   0  |    0   0  |   74.40  130 |   73.45  145 |   73.31  145  HORIZON
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 141  CS Fullerton            =  73.51   17  12   71.54( 162)    0   0  |    0   2  |   73.14  150 |   73.16  151 |   73.78  140  BIG WEST
 142  Richmond                =  73.50   15  18   73.56( 115)    0   0  |    0   1  |   73.76  139 |   74.41  133 |   72.82  153  ATLANTIC 10
 143  Hawai'i                 =  73.49   21  11   69.41( 257)    0   0  |    0   0  |   73.79  138 |   74.62  128 |   72.69  155  BIG WEST
 144  UC Riverside            =  73.47   21  11   71.36( 172)    0   1  |    0   2  |   73.60  144 |   73.93  141 |   73.07  149  BIG WEST
 145  Eastern Washington      =  73.43   21  10   70.01( 235)    0   0  |    0   1  |   73.48  146 |   73.97  140 |   73.04  150  BIG SKY
 146  Florida State           =  73.22    9  23   78.25(  55)    0   2  |    1   9  |   72.82  156 |   73.20  150 |   73.33  144  ATLANTIC COAST
 147  Minnesota               =  73.20    9  22   79.89(  27)    0   6  |    2  15  |   72.15  163 |   72.54  163 |   73.97  135  BIG TEN
 148  Troy                    =  73.08   17  13   71.49( 165)    0   1  |    0   2  |   73.64  143 |   73.21  149 |   72.63  156  SUN BELT
 149  Kennesaw State          =  73.08   23   8   69.70( 245)    0   1  |    0   2  |   72.37  162 |   72.82  158 |   73.46  142  ATLANTIC SUN
 150  South Florida           =  73.06   14  18   73.79( 108)    0   1  |    0   4  |   73.21  148 |   73.05  155 |   72.90  151  AMER. ATHLETIC
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 151  Stephen F. Austin       =  73.06   16  13   71.08( 182)    0   0  |    0   0  |   73.97  136 |   73.72  144 |   72.18  160  WESTERN ATHLETIC
 152  Saint Joseph's-Pa.      =  72.90   16  17   72.19( 142)    0   1  |    0   2  |   71.95  166 |   71.42  179 |   74.04  134  ATLANTIC 10
 153  NC Asheville            =  72.84   25   7   67.90( 303)    0   1  |    0   1  |   71.26  182 |   73.38  147 |   73.26  147  BIG SOUTH
 154  Georgia                 =  72.82   16  16   76.76(  78)    1   5  |    3   6  |   73.66  142 |   75.49  120 |   71.02  182  SOUTHEASTERN
 155  NC Wilmington           =  72.82   22  10   70.48( 209)    0   1  |    0   2  |   71.89  168 |   73.72  143 |   72.75  154  COLONIAL
 156  Ball State              =  72.68   18  12   70.40( 214)    0   0  |    0   0  |   73.20  149 |   73.09  154 |   72.13  162  MAC
 157  SMU                     =  72.67   10  22   77.18(  75)    0   4  |    1   6  |   72.58  159 |   72.68  160 |   72.62  157  AMER. ATHLETIC
 158  Northern Kentucky       =  72.62   20  12   69.21( 266)    0   0  |    0   1  |   71.37  177 |   72.64  161 |   73.14  148  HORIZON
 159  Cornell                 =  72.56   15  10   71.03( 185)    0   0  |    0   1  |   72.90  154 |   72.91  157 |   72.11  163  IVY LEAGUE
 160  Old Dominion            =  72.45   18  12   71.49( 166)    0   0  |    0   0  |   72.49  161 |   72.72  159 |   72.21  159  SUN BELT
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 161  South Carolina          =  72.41   11  21   78.10(  59)    1   5  |    2   8  |   71.02  186 |   71.89  171 |   73.26  146  SOUTHEASTERN
 162  Portland                =  72.26   12  19   75.57(  92)    0   5  |    1   7  |   72.79  157 |   72.46  164 |   71.80  165  WEST COAST
 163  South Dakota State      =  72.20   18  13   70.29( 217)    0   2  |    0   2  |   72.79  158 |   72.98  156 |   71.41  172  SUMMIT LEAGUE
 164  Chattanooga             =  72.18   15  17   71.06( 184)    0   0  |    0   0  |   71.40  175 |   71.37  181 |   72.88  152  SOUTHERN
 165  East Carolina           =  72.14   16  16   73.41( 116)    0   1  |    0   2  |   71.28  181 |   72.03  168 |   72.54  158  AMER. ATHLETIC
 166  Seattle                 =  72.09   18  12   72.18( 143)    0   0  |    0   1  |   73.09  151 |   73.41  146 |   70.83  185  WESTERN ATHLETIC
 167  Wyoming                 =  72.09    8  22   76.46(  84)    0   1  |    0   5  |   73.03  152 |   72.59  162 |   71.27  177  MOUNTAIN WEST
 168  Western Kentucky        =  72.07   15  16   73.23( 118)    0   0  |    0   3  |   72.87  155 |   73.13  152 |   71.04  181  CONFERENCE USA
 169  Harvard                 =  72.01   12  14   71.17( 179)    0   1  |    0   1  |   71.92  167 |   71.59  176 |   72.17  161  IVY LEAGUE
 170  St. Bonaventure         =  71.94   14  18   72.41( 138)    0   0  |    0   0  |   72.05  164 |   72.38  165 |   71.56  167  ATLANTIC 10
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 171  Louisiana Tech          =  71.93   12  18   73.76( 109)    0   0  |    0   3  |   73.48  145 |   72.31  166 |   70.87  184  CONFERENCE USA
 172  Oregon State            =  71.65   10  21   78.22(  57)    0   5  |    1   8  |   71.89  169 |   71.71  174 |   71.41  173  PAC-12
 173  New Mexico State        =  71.61    6  15   74.07( 105)    0   1  |    0   1  |   72.49  160 |   71.94  170 |   70.90  183  WESTERN ATHLETIC
 174  Northern Iowa           =  71.47   13  18   72.56( 134)    0   0  |    0   0  |   71.57  173 |   71.29  182 |   71.42  171  MISSOURI VALLEY
 175  Georgetown              =  71.38    7  25   79.49(  34)    0   8  |    0  15  |   71.35  179 |   70.89  188 |   71.54  169  BIG EAST
 176  Lipscomb                =  71.36   17  13   69.36( 262)    0   0  |    0   1  |   71.14  185 |   71.16  183 |   71.48  170  ATLANTIC SUN
 177  Brown                   =  71.36   14  13   70.98( 188)    0   1  |    0   2  |   70.44  197 |   70.60  193 |   72.09  164  IVY LEAGUE
 178  Air Force               =  71.34   14  18   72.74( 126)    0   0  |    0   4  |   71.72  171 |   70.69  191 |   71.37  174  MOUNTAIN WEST
 179  Wright State            =  71.32   16  15   68.49( 287)    0   0  |    0   0  |   71.36  178 |   70.59  194 |   71.56  166  HORIZON
 180  California Baptist      =  71.22   15  16   70.78( 198)    0   0  |    0   0  |   71.85  170 |   71.55  177 |   70.63  187  WESTERN ATHLETIC
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 181  Long Beach State        =  71.19   15  16   71.58( 160)    0   1  |    0   2  |   71.96  165 |   71.94  169 |   70.33  196  BIG WEST
 182  Navy                    =  71.03   17  13   67.38( 315)    0   1  |    0   1  |   70.67  190 |   70.15  202 |   71.55  168  PATRIOT
 183  UC Davis                =  71.02   16  14   70.25( 219)    0   1  |    0   1  |   71.68  172 |   71.86  172 |   70.17  200  BIG WEST
 184  Massachusetts           =  70.97   15  16   73.11( 122)    0   0  |    0   0  |   71.29  180 |   72.23  167 |   70.07  203  ATLANTIC 10
 185  UTEP                    =  70.92   12  18   73.19( 120)    0   1  |    0   3  |   71.49  174 |   70.90  187 |   70.56  190  CONFERENCE USA
 186  Montana                 =  70.89   16  14   70.14( 225)    0   2  |    0   2  |   71.40  176 |   71.45  178 |   70.26  198  BIG SKY
 187  Drexel                  =  70.83   16  15   68.48( 288)    0   0  |    0   0  |   70.68  189 |   70.14  204 |   71.15  179  COLONIAL
 188  George Washington       =  70.83   15  16   72.01( 151)    0   0  |    0   0  |   70.37  198 |   70.35  197 |   71.19  178  ATLANTIC 10
 189  Cleveland State         =  70.76   20  12   68.72( 281)    0   0  |    0   0  |   70.59  194 |   71.42  180 |   70.42  193  HORIZON
 190  Longwood                =  70.73   18  12   66.81( 324)    0   1  |    0   1  |   71.00  187 |   70.56  195 |   70.57  189  BIG SOUTH
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 191  Weber State             =  70.72   16  15   70.82( 196)    0   0  |    1   0  |   70.78  188 |   70.51  196 |   70.70  186  BIG SKY
 192  Buffalo                 =  70.65   13  17   73.85( 107)    0   3  |    0   3  |   71.22  184 |   71.68  175 |   69.73  208  MAC
 193  Eastern Kentucky        =  70.59   17  13   70.03( 233)    0   1  |    0   1  |   69.85  206 |   70.05  206 |   71.13  180  ATLANTIC SUN
 194  Murray State            =  70.58   16  15   72.70( 129)    1   0  |    1   0  |   69.87  203 |   71.76  173 |   70.23  199  MISSOURI VALLEY
 195  Appalachian State       =  70.57   13  16   71.50( 164)    0   0  |    0   0  |   70.62  192 |   70.78  189 |   70.35  195  SUN BELT
 196  La Salle                =  70.50   15  19   72.50( 137)    0   0  |    0   1  |   69.46  214 |   69.61  213 |   71.35  175  ATLANTIC 10
 197  Texas State             =  70.46   14  18   71.94( 154)    0   0  |    0   0  |   70.51  196 |   70.92  186 |   70.11  202  SUN BELT
 198  Texas A&M-CorpusChristi =  70.25   19  10   64.08( 358)    0   1  |    0   3  |   69.93  201 |   69.68  211 |   70.59  188  SOUTHLAND
 199  Georgia Southern        =  70.17   14  16   70.65( 204)    0   0  |    0   0  |   69.85  207 |   69.53  214 |   70.54  191  SUN BELT
 200  Mercer                  =  70.11   12  19   70.42( 212)    0   0  |    0   0  |   69.09  224 |   68.52  229 |   71.28  176  SOUTHERN
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 201  Wofford                 =  70.06   14  16   70.97( 190)    1   0  |    1   0  |   69.59  212 |   69.63  212 |   70.41  194  SOUTHERN
 202  Tarleton State          =  70.03   13  16   73.71( 111)    0   1  |    0   1  |   70.63  191 |   70.97  185 |   69.14  219  WESTERN ATHLETIC
 203  Pepperdine              =  69.99    7  22   75.44(  95)    0   4  |    0   4  |   71.23  183 |   70.32  199 |   69.08  220  WEST COAST
 204  Radford                 =  69.98   17  14   68.86( 276)    0   2  |    0   2  |   70.61  193 |   69.92  207 |   69.60  212  BIG SOUTH
 205  Pacific                 =  69.95   14  17   73.34( 117)    0   2  |    0   2  |   69.85  205 |   70.23  200 |   69.75  206  WEST COAST
 206  Utah Tech               =  69.91   11  19   72.71( 128)    0   1  |    0   2  |   70.56  195 |   69.04  221 |   69.92  205  WESTERN ATHLETIC
 207  Norfolk State           =  69.88   17  10   65.44( 346)    0   3  |    0   3  |   69.61  211 |   69.76  210 |   69.98  204  MEAC
 208  Rider                   =  69.81   15  14   68.08( 297)    0   0  |    0   2  |   69.52  213 |   69.26  219 |   70.13  201  METRO ATLANTIC
 209  Loyola-Chicago          =  69.78   10  21   73.58( 114)    0   1  |    1   1  |   69.70  210 |   70.11  205 |   69.55  213  ATLANTIC 10
 210  Grambling State         =  69.75   21   8   64.81( 355)    0   0  |    0   0  |   69.12  222 |   70.18  201 |   69.74  207  SOUTHWESTERN
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 211  NC Central              =  69.74   14  11   66.64( 329)    0   1  |    0   2  |   69.09  225 |   68.76  225 |   70.45  192  MEAC
 212  Detroit Mercy           =  69.73   13  19   70.14( 227)    0   0  |    0   1  |   69.87  204 |   69.50  215 |   69.68  210  HORIZON
 213  North Dakota State      =  69.67   14  17   70.42( 213)    0   2  |    0   2  |   69.27  218 |   69.77  209 |   69.72  209  SUMMIT LEAGUE
 214  Abilene Christian       =  69.37    9  17   72.53( 135)    0   2  |    0   2  |   70.32  199 |   70.34  198 |   68.28  225  WESTERN ATHLETIC
 215  Bryant                  =  69.34   15  13   69.44( 256)    0   0  |    0   1  |   70.01  200 |   69.85  208 |   68.65  221  AMERICA EAST
 216  Quinnipiac              =  69.31   19  12   68.27( 294)    0   0  |    0   1  |   69.88  202 |   70.69  192 |   68.20  226  METRO ATLANTIC
 217  Fla. International      =  69.31   12  18   72.04( 150)    0   0  |    0   3  |   69.32  217 |   68.72  227 |   69.49  214  CONFERENCE USA
 218  St. Thomas-Mn.          =  69.18   17  14   68.56( 285)    0   1  |    0   1  |   69.15  221 |   68.02  235 |   69.65  211  SUMMIT LEAGUE
 219  Western Carolina        =  69.16   15  15   70.13( 228)    0   1  |    0   1  |   67.53  239 |   68.26  231 |   70.26  197  SOUTHERN
 220  Louisville              =  68.91    4  28   78.56(  49)    0   4  |    1  12  |   68.07  232 |   68.86  223 |   69.25  217  ATLANTIC COAST
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 221  Rice                    =  68.85   15  15   72.73( 127)    0   1  |    0   3  |   69.77  209 |   71.03  184 |   67.08  248  CONFERENCE USA
 222  Siena                   =  68.82   17  15   68.80( 278)    0   0  |    0   0  |   69.37  215 |   70.14  203 |   67.73  236  METRO ATLANTIC
 223  Florida Gulf Coast      =  68.71   16  15   69.15( 269)    0   1  |    1   2  |   69.81  208 |   70.77  190 |   66.90  252  ATLANTIC SUN
 224  Stetson                 =  68.64   15  13   70.66( 203)    0   0  |    0   0  |   69.09  223 |   69.40  217 |   67.92  230  ATLANTIC SUN
 225  Gardner-Webb            =  68.64   13  16   69.20( 267)    0   0  |    0   1  |   69.36  216 |   68.77  224 |   68.10  228  BIG SOUTH
 226  Campbell                =  68.61   14  18   68.35( 292)    0   0  |    0   1  |   67.91  235 |   67.34  246 |   69.46  216  BIG SOUTH
 227  San Diego               =  68.58    9  20   73.73( 110)    0   3  |    0   4  |   69.22  220 |   69.13  220 |   67.87  234  WEST COAST
 228  Jacksonville State      =  68.50   10  18   69.85( 239)    0   1  |    0   1  |   67.69  238 |   67.69  239 |   69.18  218  ATLANTIC SUN
 229  Rhode Island            =  68.48    9  22   72.90( 123)    0   1  |    0   2  |   69.26  219 |   68.45  230 |   67.99  229  ATLANTIC 10
 230  Northern Arizona        =  68.48   10  23   71.37( 171)    0   2  |    0   2  |   67.87  236 |   66.71  250 |   69.48  215  BIG SKY
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 231  Delaware                =  68.33   16  16   70.28( 218)    0   1  |    0   1  |   68.15  231 |   69.46  216 |   67.73  237  COLONIAL
 232  East Tennessee State(ETS=  68.24   10  20   69.70( 244)    0   0  |    0   0  |   68.06  233 |   67.55  241 |   68.57  223  SOUTHERN
 233  Milwaukee               =  68.18   18  11   68.74( 279)    0   1  |    0   2  |   68.37  228 |   69.29  218 |   67.41  243  HORIZON
 234  Northern Colorado       =  68.14   12  19   70.73( 200)    0   2  |    0   2  |   67.95  234 |   68.65  228 |   67.88  233  BIG SKY
 235  Morehead State          =  68.06   17  11   66.26( 337)    0   2  |    0   2  |   67.22  244 |   69.02  222 |   67.88  232  OHIO VALLEY
 236  Winthrop                =  67.87   13  17   69.51( 253)    0   0  |    0   2  |   67.48  240 |   68.03  234 |   67.89  231  BIG SOUTH
 237  Fort Wayne(PFW)         =  67.76   15  15   68.64( 283)    0   0  |    0   2  |   68.41  227 |   68.75  226 |   66.79  255  HORIZON
 238  Northwestern State      =  67.75   21  11   65.52( 344)    1   2  |    1   3  |   68.18  229 |   68.16  233 |   67.23  246  SOUTHLAND
 239  Howard                  =  67.75   17  12   67.12( 319)    0   1  |    0   1  |   66.33  261 |   67.07  248 |   68.63  222  MEAC
 240  California              =  67.70    3  29   78.92(  44)    0   5  |    0  10  |   68.68  226 |   67.91  236 |   66.98  250  PAC-12
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 241  Northern Illinois       =  67.65   12  18   71.76( 157)    0   1  |    0   2  |   67.35  242 |   67.38  244 |   67.84  235  MAC
 242  UMBC                    =  67.59   17  14   66.61( 330)    0   1  |    0   1  |   67.75  237 |   67.83  237 |   67.30  245  AMERICA EAST
 243  Miami-Ohio              =  67.59    9  20   71.00( 186)    0   1  |    0   1  |   66.87  247 |   66.14  263 |   68.49  224  MAC
 244  Robert Morris           =  67.41   14  17   68.48( 289)    0   0  |    0   1  |   66.89  245 |   67.36  245 |   67.58  241  HORIZON
 245  Sacramento State        =  67.25   12  18   70.64( 205)    0   1  |    0   1  |   68.17  230 |   67.55  240 |   66.51  258  BIG SKY
 246  Boston U.               =  67.14   14  17   67.74( 307)    0   1  |    0   1  |   66.56  256 |   66.52  256 |   67.62  239  PATRIOT
 247  North Florida(UNF)      =  67.13   12  17   69.70( 246)    0   3  |    0   3  |   66.62  253 |   67.50  242 |   67.09  247  ATLANTIC SUN
 248  Canisius                =  67.12    9  20   69.67( 247)    0   0  |    0   1  |   66.28  262 |   65.55  277 |   68.12  227  METRO ATLANTIC
 249  Army West Point         =  67.00   15  16   66.66( 327)    0   0  |    0   0  |   66.21  263 |   66.59  254 |   67.48  242  PATRIOT
 250  USC Upstate             =  66.90   14  15   69.51( 252)    0   1  |    0   2  |   65.70  271 |   66.44  259 |   67.59  240  BIG SOUTH
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 251  Queens-NC               =  66.88   15  15   69.29( 264)    0   0  |    0   0  |   66.57  254 |   66.05  264 |   67.33  244  ATLANTIC SUN
 252  UT Arlington            =  66.87    8  21   73.61( 113)    0   0  |    0   1  |   67.45  241 |   67.45  243 |   66.17  266  WESTERN ATHLETIC
 253  Valparaiso              =  66.86   10  21   71.53( 163)    0   0  |    0   0  |   66.50  258 |   66.70  251 |   67.02  249  MISSOURI VALLEY
 254  Illinois State          =  66.79   11  21   70.18( 223)    0   0  |    0   0  |   66.67  250 |   66.58  255 |   66.86  253  MISSOURI VALLEY
 255  Niagara                 =  66.76   15  14   68.09( 296)    0   1  |    0   1  |   66.74  249 |   67.26  247 |   66.42  259  METRO ATLANTIC
 256  SE Missouri State(SEMO) =  66.73   17  16   66.21( 338)    0   0  |    0   1  |   66.54  257 |   66.24  260 |   66.96  251  OHIO VALLEY
 257  Dartmouth               =  66.67    8  18   71.27( 175)    0   0  |    0   0  |   65.71  268 |   65.33  281 |   67.64  238  IVY LEAGUE
 258  Western Illinois        =  66.51   13  14   67.93( 300)    0   0  |    0   0  |   66.67  251 |   66.64  253 |   66.27  263  SUMMIT LEAGUE
 259  Jacksonville            =  66.51   10  16   70.44( 210)    0   1  |    0   1  |   67.32  243 |   68.17  232 |   65.02  280  ATLANTIC SUN
 260  Fairfield               =  66.40   12  18   68.95( 275)    0   1  |    0   1  |   66.35  259 |   66.23  261 |   66.41  260  METRO ATLANTIC
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 261  Bellarmine              =  66.35   12  18   71.39( 170)    0   3  |    0   4  |   66.57  255 |   66.78  249 |   65.91  271  ATLANTIC SUN
 262  Oakland-Mich.           =  66.29   12  19   70.70( 201)    0   1  |    0   2  |   65.79  266 |   66.45  257 |   66.36  262  HORIZON
 263  Arkansas State          =  66.17   10  20   69.47( 254)    0   0  |    0   0  |   65.61  274 |   65.30  282 |   66.75  256  SUN BELT
 264  Lehigh                  =  66.15   14  14   67.60( 311)    0   0  |    0   0  |   65.41  277 |   66.14  262 |   66.41  261  PATRIOT
 265  Alcorn State            =  66.10   18  13   67.54( 312)    0   1  |    0   1  |   65.51  276 |   67.72  238 |   65.42  277  SOUTHWESTERN
 266  Portland State          =  65.87   10  19   71.19( 177)    0   2  |    0   2  |   66.79  248 |   66.69  252 |   64.82  285  BIG SKY
 267  Marist                  =  65.80   12  19   67.24( 316)    0   0  |    0   0  |   64.67  292 |   64.97  288 |   66.61  257  METRO ATLANTIC
 268  Illinois-Chicago        =  65.77   11  20   70.97( 191)    0   0  |    0   1  |   65.62  273 |   65.84  271 |   65.71  275  MISSOURI VALLEY
 269  New Hampshire           =  65.77   13  15   68.31( 293)    0   0  |    0   0  |   64.70  289 |   65.91  268 |   66.10  267  AMERICA EAST
 270  Lafayette               =  65.72   11  23   69.75( 242)    0   0  |    0   2  |   65.57  275 |   64.58  294 |   66.21  265  PATRIOT
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 271  Md.-Eastern Shore(UMES) =  65.69   14  12   67.67( 309)    0   1  |    0   2  |   64.58  294 |   65.37  280 |   66.26  264  MEAC
 272  Mount St. Mary's        =  65.60   12  20   69.00( 273)    0   1  |    0   2  |   65.15  281 |   64.98  287 |   66.01  270  METRO ATLANTIC
 273  SIU-Edwardsville        =  65.56   16  14   65.82( 342)    0   0  |    0   0  |   66.66  252 |   66.04  265 |   64.60  291  OHIO VALLEY
 274  Saint Peter's           =  65.54   13  17   67.97( 299)    0   1  |    0   1  |   64.32  297 |   65.46  279 |   66.04  269  METRO ATLANTIC
 275  Bowling Green           =  65.53    9  20   70.02( 234)    0   0  |    0   0  |   66.09  264 |   66.00  267 |   64.89  284  MAC
 276  Merrimack               =  65.52   16  16   64.54( 356)    0   0  |    0   1  |   63.27  312 |   64.54  296 |   66.81  254  NORTHEAST
 277  UC San Diego            =  65.47    8  20   71.40( 168)    0   0  |    0   1  |   65.25  280 |   64.66  293 |   65.86  272  BIG WEST
 278  Georgia State           =  65.45    7  21   71.07( 183)    0   0  |    0   1  |   66.89  246 |   66.44  258 |   63.98  301  SUN BELT
 279  North Alabama           =  65.43   15  14   69.39( 258)    0   0  |    0   1  |   64.72  288 |   65.91  269 |   65.43  276  ATLANTIC SUN
 280  UTSA                    =  65.34    8  22   72.59( 132)    0   0  |    0   2  |   64.62  293 |   64.95  289 |   65.78  273  CONFERENCE USA
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 281  UTRGV                   =  65.33   11  17   70.96( 192)    0   2  |    0   2  |   65.40  278 |   65.89  270 |   64.91  283  WESTERN ATHLETIC
 282  Manhattan               =  65.32   11  18   68.04( 298)    0   0  |    0   1  |   64.70  290 |   64.14  301 |   66.06  268  METRO ATLANTIC
 283  North Dakota            =  65.31   11  20   69.05( 270)    0   1  |    0   2  |   64.95  284 |   64.57  295 |   65.74  274  SUMMIT LEAGUE
 284  American U.             =  65.29   17  15   66.82( 323)    0   0  |    0   0  |   65.76  267 |   65.80  272 |   64.67  289  PATRIOT
 285  Idaho State             =  65.24    9  21   69.36( 261)    0   0  |    0   0  |   65.69  272 |   65.07  285 |   65.00  281  BIG SKY
 286  South Dakota            =  65.24   10  19   69.55( 251)    0   0  |    0   1  |   64.35  296 |   65.69  273 |   65.33  278  SUMMIT LEAGUE
 287  Coastal Carolina        =  64.96    8  20   71.17( 180)    0   0  |    0   0  |   65.97  265 |   65.59  275 |   63.97  302  SUN BELT
 288  Northeastern            =  64.92   10  20   70.22( 221)    0   0  |    0   1  |   64.51  295 |   65.58  276 |   64.69  288  COLONIAL
 289  CS Bakersfield          =  64.91    9  22   70.95( 194)    0   0  |    0   0  |   65.70  269 |   65.47  278 |   64.07  299  BIG WEST
 290  Tennessee State         =  64.89   14  14   64.05( 359)    0   0  |    0   0  |   64.91  285 |   64.86  291 |   64.81  286  OHIO VALLEY
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 291  Cal Poly-SLO            =  64.82    6  25   71.35( 173)    0   0  |    0   0  |   65.36  279 |   63.81  306 |   64.93  282  BIG WEST
 292  SE Louisiana            =  64.76   15  14   66.13( 339)    0   1  |    0   1  |   64.87  286 |   65.29  283 |   64.32  297  SOUTHLAND
 293  Tulsa                   =  64.63    5  25   75.64(  91)    0   2  |    0   4  |   65.70  270 |   66.01  266 |   63.11  313  AMER. ATHLETIC
 294  Southern U.             =  64.58   13  17   66.36( 334)    0   3  |    0   3  |   66.34  260 |   64.91  290 |   63.27  311  SOUTHWESTERN
 295  ULM                     =  64.56    8  21   72.20( 140)    0   2  |    0   2  |   64.31  298 |   65.05  286 |   64.34  295  SUN BELT
 296  Binghamton-NY           =  64.50   11  18   68.62( 284)    0   1  |    0   1  |   63.81  307 |   63.67  307 |   65.10  279  AMERICA EAST
 297  Prairie View A&M        =  64.31   11  19   66.97( 322)    0   1  |    0   3  |   65.03  282 |   64.78  292 |   63.57  306  SOUTHWESTERN
 298  High Point              =  64.30   12  17   67.89( 305)    0   0  |    0   0  |   64.15  301 |   64.52  299 |   64.16  298  BIG SOUTH
 299  Nicholls State          =  64.29   12  15   66.74( 326)    0   2  |    0   4  |   64.97  283 |   65.69  274 |   63.01  315  SOUTHLAND
 300  Eastern Michigan        =  64.26    7  23   71.95( 152)    0   0  |    0   2  |   63.90  305 |   64.02  303 |   64.46  292  MAC
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 301  Texas Southern          =  64.16   10  20   67.90( 302)    0   2  |    0   4  |   64.68  291 |   64.43  300 |   63.66  303  SOUTHWESTERN
 302  Tennessee-Martin        =  64.16   15  14   65.37( 348)    0   0  |    0   0  |   64.10  302 |   65.11  284 |   63.57  307  OHIO VALLEY
 303  Western Michigan        =  64.14    5  23   71.57( 161)    0   0  |    0   1  |   64.82  287 |   63.40  313 |   64.05  300  MAC
 304  William & Mary          =  64.12   11  20   69.63( 249)    0   0  |    0   1  |   63.36  311 |   63.97  304 |   64.45  294  COLONIAL
 305  Tennessee Tech          =  64.07   13  17   66.43( 332)    0   1  |    0   1  |   63.61  309 |   63.48  310 |   64.46  293  OHIO VALLEY
 306  Stony Brook-NY          =  64.05    9  22   69.88( 238)    0   1  |    0   1  |   63.04  314 |   63.39  314 |   64.72  287  COLONIAL
 307  Fairleigh Dickinson     =  63.87   17  15   63.30( 362)    0   0  |    0   0  |   62.37  324 |   63.38  315 |   64.66  290  NORTHEAST
 308  Denver                  =  63.79   13  17   66.97( 321)    0   1  |    0   1  |   64.19  300 |   64.52  298 |   63.09  314  SUMMIT LEAGUE
 309  Maine                   =  63.76   11  17   69.98( 236)    0   0  |    0   1  |   64.23  299 |   64.14  302 |   63.21  312  AMERICA EAST
 310  Jackson State           =  63.72   14  18   68.11( 295)    0   3  |    0   6  |   63.60  310 |   63.83  305 |   63.62  304  SOUTHWESTERN
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 311  Loyola-Maryland         =  63.65   11  20   67.61( 310)    0   0  |    0   2  |   62.51  321 |   63.11  318 |   64.32  296  PATRIOT
 312  Bucknell                =  63.61   11  20   67.05( 320)    0   0  |    0   1  |   63.82  306 |   63.46  311 |   63.49  309  PATRIOT
 313  Wagner                  =  63.42   13  13   63.88( 360)    0   0  |    0   0  |   63.06  313 |   63.66  308 |   63.37  310  NORTHEAST
 314  Southern Indiana        =  63.19   13  16   66.34( 335)    0   0  |    0   0  |   63.95  304 |   63.35  316 |   62.60  320  OHIO VALLEY
 315  NC A&T                  =  63.16   10  19   69.92( 237)    0   1  |    0   3  |   63.03  315 |   63.65  309 |   62.87  317  COLONIAL
 316  Chicago State           =  63.06    7  20   72.11( 146)    0   2  |    0   3  |   62.97  316 |   61.68  327 |   63.62  305  INDEPENDENTS
 317  Kansas City(UMKC)       =  62.94   10  20   69.34( 263)    0   1  |    0   2  |   64.01  303 |   64.52  297 |   61.23  334  SUMMIT LEAGUE
 318  Alabama A&M             =  62.90   12  17   65.42( 347)    0   0  |    0   2  |   62.37  325 |   61.82  326 |   63.52  308  SOUTHWESTERN
 319  Charleston Southern     =  62.74    8  21   69.04( 272)    0   0  |    0   1  |   62.76  319 |   62.47  322 |   62.76  319  BIG SOUTH
 320  Sacred Heart            =  62.71   15  17   63.67( 361)    0   0  |    0   1  |   62.00  327 |   62.74  319 |   62.93  316  NORTHEAST
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 321  The Citadel             =  62.69    9  22   70.48( 208)    0   0  |    0   2  |   62.55  320 |   63.24  317 |   62.37  323  SOUTHERN
 322  Omaha(Neb.-Omaha)       =  62.53    8  23   70.85( 195)    0   1  |    0   3  |   62.89  318 |   62.69  320 |   62.16  324  SUMMIT LEAGUE
 323  Little Rock             =  62.53    8  21   66.43( 333)    0   1  |    0   2  |   62.43  323 |   61.84  325 |   62.79  318  OHIO VALLEY
 324  Idaho                   =  62.38    8  22   68.50( 286)    0   0  |    0   0  |   63.63  308 |   62.59  321 |   61.44  330  BIG SKY
 325  Elon                    =  62.04    6  24   69.38( 259)    0   1  |    0   2  |   61.66  330 |   61.28  329 |   62.48  321  COLONIAL
 326  Central Michigan        =  62.04    8  21   70.96( 193)    0   1  |    1   1  |   62.91  317 |   63.45  312 |   60.56  336  MAC
 327  NJIT(New Jersey Tech)   =  61.99    6  23   68.44( 290)    0   0  |    0   0  |   61.78  328 |   61.08  333 |   62.41  322  AMERICA EAST
 328  CS Northridge           =  61.67    5  25   70.30( 216)    0   0  |    0   0  |   62.46  322 |   61.22  330 |   61.37  331  BIG WEST
 329  Saint Francis-Pa.       =  61.66   11  18   64.49( 357)    0   0  |    0   2  |   60.99  332 |   61.18  331 |   62.10  325  NORTHEAST
 330  Texas A&M-Commerce      =  61.53   12  20   66.32( 336)    0   1  |    0   1  |   61.62  331 |   60.95  335 |   61.65  327  SOUTHLAND
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 331  Morgan State            =  61.40   11  16   67.20( 318)    0   2  |    0   2  |   61.77  329 |   62.37  323 |   60.55  338  MEAC
 332  New Orleans             =  61.35   10  20   65.02( 353)    0   1  |    0   1  |   60.04  341 |   60.82  336 |   62.06  326  SOUTHLAND
 333  Albany-NY               =  61.15    6  23   69.65( 248)    0   0  |    0   3  |   60.73  334 |   61.03  334 |   61.31  332  AMERICA EAST
 334  Monmouth-NJ             =  61.01    7  26   71.40( 169)    0   0  |    0   2  |   59.32  347 |   61.36  328 |   61.45  329  COLONIAL
 335  Austin Peay             =  60.97    6  22   69.47( 255)    0   2  |    0   3  |   62.06  326 |   61.98  324 |   59.61  342  ATLANTIC SUN
 336  Hampton                 =  60.82    7  24   69.19( 268)    0   0  |    0   0  |   59.82  343 |   59.76  344 |   61.62  328  COLONIAL
 337  Stonehill               =  60.76   13  17   65.78( 343)    0   1  |    0   2  |   60.21  338 |   59.86  342 |   61.31  333  NORTHEAST
 338  McNeese State           =  60.47   10  23   66.53( 331)    0   3  |    0   4  |   60.84  333 |   60.22  340 |   60.31  340  SOUTHLAND
 339  Holy Cross              =  60.41    8  22   67.39( 314)    0   1  |    0   1  |   59.86  342 |   60.46  339 |   60.55  337  PATRIOT
 340  Presbyterian College    =  60.33    3  27   68.73( 280)    0   0  |    0   0  |   60.63  335 |   59.11  348 |   60.61  335  BIG SOUTH
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 341  Columbia                =  60.12    5  22   70.68( 202)    0   0  |    0   2  |   59.38  346 |   60.04  341 |   60.41  339  IVY LEAGUE
 342  Central Connecticut St. =  60.11   10  22   64.89( 354)    0   0  |    0   1  |   60.14  339 |   59.66  345 |   60.21  341  NORTHEAST
 343  Central Arkansas        =  59.77    8  22   69.26( 265)    0   1  |    0   1  |   60.05  340 |   60.52  338 |   59.11  347  ATLANTIC SUN
 344  Evansville              =  59.70    5  27   72.52( 136)    0   0  |    0   0  |   60.22  337 |   61.12  332 |   58.41  351  MISSOURI VALLEY
 345  Ark.-Pine Bluff         =  59.49    6  21   67.89( 304)    0   2  |    0   3  |   60.39  336 |   59.06  349 |   59.10  348  SOUTHWESTERN
 346  VMI                     =  59.46    4  25   71.00( 187)    0   0  |    0   0  |   59.55  345 |   59.76  343 |   59.17  346  SOUTHERN
 347  Bethune-Cookman         =  59.34   10  20   65.51( 345)    0   1  |    0   3  |   58.98  349 |   59.42  347 |   59.38  344  SOUTHWESTERN
 348  Coppin State            =  59.32    9  23   70.22( 222)    0   1  |    0   3  |   59.76  344 |   60.59  337 |   58.19  353  MEAC
 349  St. Francis-NY          =  59.21   12  16   63.18( 363)    0   0  |    0   1  |   58.68  352 |   59.55  346 |   59.19  345  NORTHEAST
 350  Incarnate Word          =  58.83    9  19   65.19( 350)    0   1  |    0   1  |   58.92  350 |   58.47  351 |   58.87  349  SOUTHLAND
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 351  Eastern Illinois        =  58.74    7  22   65.98( 340)    0   0  |    1   2  |   58.78  351 |   58.59  350 |   58.70  350  OHIO VALLEY
 352  Florida A&M             =  58.30    5  22   68.38( 291)    0   2  |    0   4  |   58.35  353 |   58.17  353 |   58.25  352  SOUTHWESTERN
 353  IUPUI                   =  58.14    3  27   67.93( 301)    0   0  |    0   1  |   56.39  358 |   55.88  359 |   59.47  343  HORIZON
 354  Lindenwood              =  57.95    8  21   66.80( 325)    0   0  |    0   1  |   57.87  354 |   57.59  354 |   58.07  354  OHIO VALLEY
 355  Alabama State           =  57.80    7  23   67.42( 313)    0   0  |    0   2  |   58.98  348 |   58.36  352 |   56.62  358  SOUTHWESTERN
 356  Lamar                   =  57.37    6  22   65.21( 349)    0   1  |    0   1  |   57.12  356 |   56.56  357 |   57.75  355  SOUTHLAND
 357  SC State                =  57.30    4  26   70.08( 231)    0   1  |    0   2  |   57.50  355 |   56.98  356 |   57.26  356  MEAC
 358  Houston Christian       =  56.93    7  22   65.18( 351)    0   1  |    0   2  |   56.76  357 |   57.14  355 |   56.80  357  SOUTHLAND
 359  MVSU(Miss. Valley St.)  =  56.26    5  27   68.65( 282)    0   2  |    0   3  |   56.23  360 |   55.42  361 |   56.55  359  SOUTHWESTERN
 360  Delaware State          =  56.00    5  23   67.77( 306)    0   1  |    0   3  |   56.24  359 |   55.58  360 |   55.97  360  MEAC
College Basketball 2022-2023    Div I games only    through games of 2023 March 9 Thursday                                                      
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.09]                                               [  3.13]       [  3.23]       [  2.80]
 361  Green Bay               =  55.55    3  29   70.57( 207)    0   0  |    0   0  |   55.55  361 |   55.93  358 |   55.24  361  HORIZON
 362  Hartford                =  54.33    2  23   65.91( 341)    0   0  |    0   0  |   53.96  362 |   54.47  362 |   54.33  362  INDEPENDENTS
 363  Long Island U.(LIU)     =  52.46    1  26   66.65( 328)    0   2  |    0   2  |   52.36  363 |   52.17  363 |   52.55  363  NORTHEAST
    """    

elif config.date == 2017:
    lineparts = ["Rank","Team","Rating","W","L","Schedule","ScheduleRank","WinsVsTop25","LossesVsTop25","WinsVsTop50","LossesVsTop50",
                 "PREDICTOR","PREDICTOR_RANK",
                 "GOLDENMEAN_SCORE","GOLDENMEAN_RANK",
                 "RECENT","RECENT_RANK"]
    text = """
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
   1  Gonzaga                 =  94.62   32   1   72.38( 122)    6   0  |    6   0  |   94.69    1 |   94.47    1 |   94.53    2
   2  Villanova               =  93.93   31   3   80.14(  27)    3   0  |   13   3  |   93.67    2 |   94.36    2 |   94.60    1
   3  North Carolina          =  93.32   26   7   81.79(  10)    7   4  |   12   6  |   93.66    3 |   92.79    4 |   92.38    5
   4  West Virginia           =  92.84   26   8   80.08(  29)    6   4  |   11   6  |   93.13    4 |   92.38    6 |   92.05    6
   5  Kentucky                =  92.73   29   5   79.73(  35)    2   4  |    8   4  |   92.70    5 |   92.75    5 |   92.74    4
   6  Kansas                  =  91.98   28   4   81.83(   8)    8   2  |   14   4  |   91.53    9 |   92.79    3 |   93.05    3
   7  Louisville              =  91.98   24   8   81.86(   7)    5   7  |   11   8  |   92.25    6 |   91.54    8 |   91.20    8
   8  Duke                    =  91.73   27   8   81.90(   6)    8   4  |   15   7  |   91.56    8 |   91.98    7 |   91.93    7
   9  Virginia                =  91.23   22  10   81.83(   9)    4   6  |    7   9  |   91.70    7 |   90.53   10 |   89.95   14
  10  Florida                 =  91.00   24   8   80.59(  20)    1   4  |    6   8  |   91.22   10 |   90.62    9 |   90.43    9
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
  11  Wichita State           =  90.45   29   4   72.47( 120)    0   2  |    0   3  |   90.98   11 |   89.67   16 |   89.24   17
  12  Purdue                  =  90.22   25   7   78.90(  48)    2   4  |    9   5  |   90.39   12 |   89.93   13 |   89.67   15
  13  Oregon                  =  90.11   28   5   77.72(  63)    2   3  |    4   3  |   90.05   13 |   90.19   12 |   90.27   12
  14  Baylor                  =  89.75   24   7   82.50(   5)    6   4  |   13   7  |   89.46   16 |   90.21   11 |   90.41   10
  15  UCLA                    =  89.62   29   4   76.00(  74)    4   3  |    5   3  |   89.51   14 |   89.77   14 |   90.06   13
  16  Iowa State              =  89.43   23  10   82.90(   4)    6   6  |   13   8  |   89.47   15 |   89.32   17 |   89.31   16
  17  Wisconsin               =  89.01   25   9   80.00(  32)    1   4  |   10   7  |   89.11   17 |   88.81   18 |   88.33   20
  18  Arizona                 =  88.79   30   4   77.55(  65)    3   3  |    5   4  |   88.27   21 |   89.74   15 |   90.34   11
  19  SMU                     =  88.73   30   4   74.93(  80)    2   2  |    3   2  |   88.68   19 |   88.79   19 |   89.10   18
  20  Florida State           =  88.67   25   8   80.00(  31)    5   4  |   13   5  |   88.87   18 |   88.32   21 |   88.25   22
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
  21  Cincinnati              =  88.45   29   5   74.88(  83)    2   2  |    3   4  |   88.44   20 |   88.43   20 |   88.32   21
  22  Notre Dame              =  87.86   25   9   80.81(  16)    4   8  |   10   8  |   87.66   24 |   88.16   22 |   88.36   19
  23  Michigan                =  87.79   24  11   80.23(  26)    5   2  |   10   8  |   87.88   22 |   87.61   23 |   87.74   24
  24  Oklahoma State          =  87.58   19  12   83.01(   2)    2   9  |    8  11  |   87.73   23 |   87.32   26 |   87.36   26
  25  Saint Mary's-Cal.       =  87.54   28   4   71.62( 133)    0   3  |    1   3  |   87.63   25 |   87.36   25 |   87.39   25
  26  Butler                  =  87.29   23   8   80.78(  17)    4   0  |   13   4  |   87.12   26 |   87.54   24 |   87.76   23
  27  Creighton               =  87.13   24   9   79.40(  41)    1   3  |    6   7  |   87.08   27 |   87.18   27 |   87.14   27
  28  Miami-Florida           =  85.14   21  11   80.29(  25)    3   8  |    6  11  |   85.05   29 |   85.26   28 |   85.34   28
  29  Indiana                 =  84.70   18  15   79.82(  34)    2   8  |    4  12  |   85.12   28 |   84.04   34 |   83.37   41
  30  Marquette               =  84.70   19  12   79.64(  38)    1   3  |    7   7  |   85.01   30 |   84.19   32 |   84.19   31
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
  31  South Carolina          =  84.60   21  10   78.63(  53)    2   2  |    3   6  |   84.78   31 |   84.29   31 |   84.13   32
  32  Xavier-Ohio             =  84.30   21  13   80.71(  19)    0   4  |    6  11  |   84.23   33 |   84.37   30 |   84.02   33
  33  Minnesota               =  84.21   24   9   78.75(  50)    2   4  |    8   7  |   83.91   36 |   84.67   29 |   85.21   29
  34  Kansas State            =  84.15   20  13   80.88(  15)    4   8  |    6  11  |   84.30   32 |   83.88   35 |   83.77   36
  35  Wake Forest             =  83.87   19  13   80.53(  22)    1   7  |    3  13  |   84.05   35 |   83.55   39 |   83.72   38
  36  Michigan State          =  83.69   19  14   80.72(  18)    3   7  |    6  10  |   83.57   37 |   83.85   36 |   83.66   39
  37  Arkansas                =  83.65   25   9   77.80(  60)    0   5  |    3   7  |   83.40   42 |   84.05   33 |   84.25   30
  38  Syracuse                =  83.51   18  14   79.22(  44)    3   5  |    6   8  |   84.08   34 |   82.63   49 |   82.03   52
  39  Northwestern            =  83.46   23  11   78.69(  51)    2   4  |    6   9  |   83.31   44 |   83.67   38 |   83.83   35
  40  Dayton                  =  83.44   23   7   74.63(  87)    0   1  |    4   3  |   83.41   41 |   83.46   40 |   83.36   42
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
  41  Clemson                 =  83.34   17  15   81.23(  14)    0   8  |    3  13  |   83.45   38 |   83.14   42 |   83.07   43
  42  Maryland                =  83.18   23   8   78.40(  54)    2   2  |    7   4  |   82.79   48 |   83.83   37 |   83.97   34
  43  Vanderbilt              =  83.16   19  15   80.58(  21)    4   2  |    6   8  |   83.39   43 |   82.77   44 |   82.68   46
  44  TCU                     =  83.15   18  15   81.69(  11)    2  11  |    4  13  |   83.44   39 |   82.67   46 |   82.63   48
  45  Utah                    =  83.08   18  11   75.43(  77)    0   4  |    0   6  |   83.30   45 |   82.72   45 |   82.60   49
  46  Texas Tech              =  83.00   18  14   78.90(  47)    2   8  |    4  10  |   83.41   40 |   82.33   50 |   81.84   55
  47  Virginia Tech           =  82.93   22  10   79.44(  40)    3   6  |    8   8  |   82.63   49 |   83.40   41 |   83.76   37
  48  Rhode Island            =  82.86   24   9   74.87(  84)    1   1  |    3   3  |   82.97   46 |   82.64   47 |   82.71   45
  49  Seton Hall              =  82.61   21  11   80.07(  30)    0   4  |    6   8  |   82.29   51 |   83.12   43 |   83.42   40
  50  VCU(Va. Commonwealth)   =  82.48   26   8   74.64(  86)    0   1  |    1   4  |   82.36   50 |   82.64   48 |   82.77   44
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
  51  Houston                 =  82.35   21  10   74.30(  88)    0   4  |    1   5  |   82.83   47 |   81.59   56 |   81.24   58
  52  California              =  82.05   21  12   76.73(  71)    0   7  |    2   9  |   82.12   52 |   81.92   53 |   81.68   57
  53  Georgia                 =  81.73   18  14   80.37(  23)    0   6  |    1  11  |   81.62   53 |   81.86   54 |   81.76   56
  54  Illinois State          =  81.61   26   6   72.67( 114)    1   2  |    1   3  |   81.22   58 |   82.26   51 |   82.66   47
  55  Southern California     =  81.60   24   9   75.44(  76)    2   6  |    2   7  |   81.23   57 |   82.21   52 |   82.54   50
  56  Nevada                  =  81.50   28   6   72.78( 111)    0   1  |    0   1  |   81.31   55 |   81.77   55 |   82.13   51
  57  Alabama                 =  81.42   19  14   77.85(  59)    0   4  |    3   7  |   81.57   54 |   81.15   59 |   81.12   59
  58  Providence              =  81.27   20  12   78.98(  45)    0   3  |    7   8  |   81.10   59 |   81.50   57 |   81.89   54
  59  Georgetown              =  81.00   14  18   80.11(  28)    1   4  |    5  12  |   81.25   56 |   80.58   60 |   80.12   63
  60  Middle Tennessee        =  80.99   29   4   70.07( 178)    0   0  |    1   1  |   80.74   62 |   81.38   58 |   81.89   53
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
  61  Oklahoma                =  80.77   11  20   83.06(   1)    1  12  |    5  16  |   81.09   60 |   80.24   64 |   79.62   71
  62  Ohio State              =  80.56   17  15   78.07(  58)    2   4  |    4  10  |   80.69   63 |   80.33   63 |   79.99   64
  63  Texas A&M               =  80.49   16  15   78.38(  55)    0   6  |    1  12  |   80.63   64 |   80.22   65 |   79.74   68
  64  Texas                   =  80.47   11  22   82.98(   3)    2  10  |    4  17  |   80.96   61 |   79.70   70 |   78.79   76
  65  Tennessee               =  80.14   15  16   80.36(  24)    1   6  |    3  10  |   80.37   65 |   79.75   69 |   79.69   69
  66  Iowa                    =  80.13   18  14   78.63(  52)    4   3  |    6   9  |   79.94   67 |   80.41   62 |   80.52   61
  67  Colorado                =  80.09   18  14   76.40(  72)    1   5  |    2   7  |   80.12   66 |   80.03   67 |   79.89   65
  68  NC Wilmington           =  79.91   27   5   71.26( 141)    0   0  |    0   1  |   79.58   70 |   80.45   61 |   80.96   60
  69  Illinois                =  79.72   17  14   79.67(  37)    1   6  |    5  10  |   79.46   71 |   80.11   66 |   80.45   62
  70  Pittsburgh              =  79.57   16  17   81.29(  13)    2   9  |    5  14  |   79.35   73 |   79.91   68 |   79.89   66
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
  71  BYU                     =  79.49   22  11   72.09( 127)    1   4  |    1   4  |   79.71   68 |   79.11   74 |   78.82   75
  72  Central Florida(UCF)    =  79.42   21  11   74.03(  89)    1   4  |    1   4  |   79.65   69 |   79.01   75 |   79.20   73
  73  Princeton               =  79.39   22   6   70.33( 166)    0   0  |    0   1  |   79.36   72 |   79.40   72 |   79.52   72
  74  Mississippi             =  79.25   20  13   77.35(  68)    0   3  |    2   8  |   79.07   74 |   79.53   71 |   79.66   70
  75  Vermont                 =  78.76   28   5   67.62( 266)    0   0  |    0   2  |   78.44   76 |   79.25   73 |   79.78   67
  76  San Diego State         =  78.48   18  14   72.94( 109)    0   1  |    0   1  |   78.68   75 |   78.13   79 |   77.65   83
  77  East Tennessee State(ETS=  78.32   25   7   69.47( 197)    0   0  |    0   1  |   78.43   77 |   78.12   80 |   78.40   79
  78  Auburn                  =  78.18   18  14   77.43(  66)    0   3  |    2   6  |   78.04   79 |   78.37   77 |   78.46   78
  79  Connecticut             =  78.02   15  17   77.22(  70)    0   7  |    1   7  |   78.21   78 |   77.68   83 |   77.16   87
  80  Georgia Tech            =  77.91   16  15   79.71(  36)    3   4  |    6   9  |   77.42   83 |   78.71   76 |   79.16   74
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
  81  Penn State              =  77.82   15  18   79.29(  43)    0   6  |    3  11  |   77.84   80 |   77.76   81 |   77.79   82
  82  Texas-Arlington         =  77.57   23   8   70.59( 160)    1   0  |    1   2  |   77.45   82 |   77.71   82 |   77.85   81
  83  Monmouth-NJ             =  77.56   27   6   68.76( 227)    0   1  |    0   3  |   77.20   85 |   78.15   78 |   78.64   77
  84  Davidson                =  77.54   17  15   75.36(  78)    0   2  |    2   8  |   77.66   81 |   77.31   87 |   77.15   88
  85  Colorado State          =  77.38   21  11   73.24( 102)    0   1  |    0   2  |   77.29   84 |   77.50   85 |   77.86   80
  86  NC State                =  77.30   15  17   78.86(  49)    1   6  |    2  14  |   77.07   88 |   77.63   84 |   77.32   85
  87  Memphis                 =  77.13   19  13   74.02(  91)    0   3  |    1   3  |   77.00   90 |   77.33   86 |   77.12   89
  88  Stanford                =  77.12   13  17   79.32(  42)    0   8  |    2  10  |   77.15   86 |   77.05   91 |   76.85   97
  89  St. Bonaventure         =  77.10   20  12   72.16( 126)    0   1  |    0   6  |   77.10   87 |   77.07   90 |   77.06   91
  90  St. John's              =  76.91   14  19   79.99(  33)    0   3  |    4  13  |   76.89   91 |   76.90   92 |   76.99   93
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
  91  Mississippi State       =  76.90   16  16   76.06(  73)    0   2  |    1   5  |   77.03   89 |   76.65   96 |   76.44   99
  92  Valparaiso              =  76.87   23   8   69.24( 206)    0   2  |    1   2  |   76.60   94 |   77.28   88 |   77.24   86
  93  Richmond                =  76.67   20  12   73.96(  92)    0   0  |    1   7  |   76.40   96 |   77.09   89 |   77.38   84
  94  Bucknell                =  76.65   26   8   67.82( 260)    0   0  |    1   2  |   76.67   92 |   76.58   98 |   76.95   95
  95  Boise State             =  76.64   18  11   73.84(  93)    1   1  |    1   1  |   76.63   93 |   76.63   97 |   76.57   98
  96  Belmont                 =  76.47   21   6   69.03( 217)    0   1  |    0   3  |   76.23   98 |   76.82   95 |   77.02   92
  97  New Mexico State        =  76.40   25   5   67.11( 283)    0   0  |    0   0  |   76.12   99 |   76.82   94 |   76.98   94
  98  Akron                   =  76.23   25   8   69.95( 182)    0   1  |    0   2  |   75.85  102 |   76.84   93 |   77.09   90
  99  Nebraska                =  76.13   11  19   81.46(  12)    1   5  |    4  13  |   76.30   97 |   75.82  102 |   75.63  102
 100  Louisiana Tech          =  76.07   21  10   67.14( 282)    0   0  |    0   1  |   76.57   95 |   75.24  104 |   75.00  109
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 101  College of Charleston   =  75.98   24   9   71.17( 142)    0   1  |    0   2  |   75.67  105 |   76.47   99 |   76.95   96
 102  Fresno State            =  75.83   18  12   73.29( 100)    0   1  |    0   2  |   75.74  103 |   75.95  100 |   76.12  100
 103  Oakland-Mich.           =  75.79   22   8   67.92( 255)    0   0  |    0   1  |   75.68  104 |   75.94  101 |   76.01  101
 104  Ohio                    =  75.64   19  11   69.77( 189)    0   0  |    0   0  |   75.89  100 |   75.22  105 |   75.05  108
 105  Temple                  =  75.58   16  16   74.92(  81)    2   5  |    2   5  |   75.56  106 |   75.59  103 |   75.40  105
 106  Loyola-Chicago          =  75.39   16  14   71.72( 131)    0   2  |    0   2  |   75.88  101 |   74.58  110 |   74.36  116
 107  San Francisco           =  74.82   19  12   70.81( 152)    0   4  |    1   4  |   75.03  107 |   74.46  113 |   74.64  111
 108  New Mexico              =  74.77   17  14   73.80(  94)    0   1  |    0   3  |   74.51  110 |   75.15  107 |   75.09  106
 109  Harvard                 =  74.71   16  10   69.95( 181)    0   0  |    0   0  |   74.77  108 |   74.59  109 |   74.53  113
 110  George Mason            =  74.69   19  13   73.01( 106)    0   0  |    0   5  |   74.50  111 |   74.98  108 |   75.40  104
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 111  Arizona State           =  74.56   15  18   77.72(  62)    0   8  |    0  10  |   74.54  109 |   74.56  112 |   74.52  114
 112  George Washington       =  74.48   19  14   74.02(  90)    0   1  |    1   5  |   74.03  112 |   75.21  106 |   75.61  103
 113  Florida Gulf Coast      =  74.15   23   7   66.98( 290)    0   2  |    0   3  |   73.94  115 |   74.45  114 |   74.78  110
 114  Winthrop                =  74.03   24   6   65.42( 319)    0   1  |    0   2  |   73.68  122 |   74.57  111 |   75.07  107
 115  CS Bakersfield          =  74.02   19   9   68.34( 241)    0   2  |    0   2  |   73.97  114 |   74.07  116 |   74.38  115
 116  NC Asheville            =  73.99   21   9   66.87( 295)    0   1  |    0   2  |   73.86  118 |   74.17  115 |   74.56  112
 117  Towson                  =  73.97   19  13   70.95( 148)    0   0  |    0   1  |   73.98  113 |   73.91  117 |   74.00  117
 118  Santa Clara             =  73.78   16  16   72.32( 123)    0   6  |    0   7  |   73.92  116 |   73.50  121 |   73.55  122
 119  Rutgers                 =  73.75   14  18   78.20(  57)    0   4  |    0  14  |   73.81  119 |   73.62  118 |   73.79  118
 120  Utah State              =  73.71   13  17   73.53(  97)    0   1  |    0   2  |   73.91  117 |   73.36  123 |   73.22  125
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 121  Old Dominion            =  73.62   19  12   70.06( 179)    0   1  |    0   3  |   73.60  124 |   73.62  120 |   73.60  119
 122  Missouri State          =  73.53   16  16   71.75( 130)    0   3  |    0   3  |   73.74  120 |   73.16  126 |   72.84  133
 123  Iona                    =  73.53   22  12   69.13( 212)    0   1  |    0   1  |   73.59  125 |   73.39  122 |   73.39  123
 124  Furman                  =  73.46   19  11   69.26( 204)    0   1  |    0   1  |   73.71  121 |   73.02  130 |   73.22  126
 125  UC Irvine               =  73.34   19  14   69.23( 207)    0   2  |    0   2  |   73.63  123 |   72.84  133 |   72.50  141
 126  La Salle                =  73.27   15  15   73.68(  96)    0   1  |    1   4  |   73.04  134 |   73.62  119 |   73.58  121
 127  Washington              =  73.27    9  22   77.75(  61)    0   6  |    0  10  |   73.54  126 |   72.79  135 |   72.07  150
 128  Lehigh                  =  73.25   19  12   68.72( 229)    0   0  |    0   1  |   73.37  128 |   73.03  129 |   73.06  129
 129  Buffalo                 =  73.25   15  15   71.44( 137)    0   0  |    0   2  |   73.36  129 |   73.04  128 |   73.07  128
 130  Tulsa                   =  73.23   15  17   75.65(  75)    0   7  |    0   7  |   73.19  132 |   73.27  124 |   73.18  127
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 131  Fort Wayne(IPFW)        =  73.20   16  12   68.91( 223)    0   1  |    1   2  |   73.41  127 |   72.83  134 |   72.51  139
 132  Chattanooga             =  73.12   17  12   69.60( 193)    0   1  |    0   2  |   73.22  131 |   72.93  131 |   72.52  138
 133  Toledo                  =  73.03   16  16   71.07( 146)    0   0  |    0   0  |   73.25  130 |   72.64  138 |   72.45  142
 134  Yale                    =  72.88   17  11   70.17( 174)    0   1  |    0   1  |   72.83  136 |   72.93  132 |   72.77  134
 135  Saint Peter's           =  72.87   19  13   68.50( 236)    0   1  |    0   2  |   73.17  133 |   72.35  143 |   72.51  140
 136  Georgia State           =  72.82   18  12   70.17( 175)    0   1  |    0   1  |   72.64  140 |   73.08  127 |   73.30  124
 137  Massachusetts           =  72.75   15  18   73.10( 104)    0   0  |    1   3  |   72.84  135 |   72.58  139 |   72.37  144
 138  Kent State              =  72.73   21  13   70.18( 173)    0   0  |    0   0  |   72.70  138 |   72.74  136 |   72.99  131
 139  Northern Iowa           =  72.72   13  16   75.09(  79)    0   3  |    0   5  |   72.43  144 |   73.18  125 |   72.92  132
 140  Arkansas State          =  72.55   19  12   69.88( 187)    0   0  |    0   2  |   72.66  139 |   72.34  145 |   72.52  137
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 141  Wyoming                 =  72.54   16  14   72.26( 124)    0   0  |    0   0  |   72.64  141 |   72.34  144 |   72.38  143
 142  William & Mary          =  72.49   15  14   71.68( 132)    0   2  |    0   3  |   72.57  142 |   72.34  146 |   72.29  145
 143  Elon                    =  72.29   16  14   70.74( 153)    0   1  |    0   1  |   72.41  145 |   72.06  148 |   72.17  147
 144  Southern Illinois       =  72.24   16  16   72.65( 116)    0   3  |    0   5  |   72.07  150 |   72.50  140 |   72.63  136
 145  Missouri                =  72.17    8  24   77.62(  64)    0   3  |    2   6  |   72.78  137 |   71.14  168 |   70.60  176
 146  Boston College          =  72.15    9  23   79.49(  39)    0   7  |    1  16  |   72.40  146 |   71.72  155 |   71.46  160
 147  Eastern Michigan        =  72.14   12  17   72.21( 125)    0   1  |    0   2  |   72.46  143 |   71.59  159 |   71.24  164
 148  Albany-NY               =  72.14   20  13   67.31( 280)    0   2  |    0   2  |   72.26  147 |   71.91  149 |   72.04  152
 149  Marshall                =  72.03   19  15   70.65( 157)    0   1  |    0   1  |   72.10  149 |   71.87  150 |   71.83  155
 150  NC Greensboro           =  71.95   22   9   69.18( 211)    0   1  |    0   2  |   71.45  161 |   72.73  137 |   73.58  120
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 151  South Dakota            =  71.94   20  11   69.34( 201)    0   1  |    0   1  |   71.63  157 |   72.42  141 |   73.03  130
 152  Evansville              =  71.83   14  17   72.72( 112)    0   3  |    0   3  |   72.14  148 |   71.28  162 |   71.13  168
 153  Northern Kentucky       =  71.82   22  10   68.40( 239)    0   1  |    0   1  |   71.64  156 |   72.10  147 |   72.70  135
 154  Louisiana-Lafayette     =  71.82   19  12   69.23( 208)    0   0  |    0   1  |   71.77  154 |   71.86  151 |   72.00  153
 155  Saint Joseph's-Pa.      =  71.80   11  20   74.78(  85)    0   1  |    0   5  |   71.90  151 |   71.62  158 |   71.17  166
 156  Rice                    =  71.77   20  11   67.33( 278)    0   0  |    0   1  |   71.84  153 |   71.63  157 |   71.78  157
 157  LSU                     =  71.75   10  21   78.97(  46)    0   3  |    0  10  |   71.33  164 |   72.38  142 |   72.20  146
 158  Grand Canyon            =  71.61   20   9   66.34( 308)    0   3  |    0   3  |   71.47  160 |   71.79  154 |   72.04  151
 159  Northeastern            =  71.56   15  16   71.80( 129)    0   0  |    1   0  |   71.74  155 |   71.24  165 |   70.98  170
 160  North Dakota State      =  71.55   17  11   69.89( 185)    0   0  |    0   2  |   71.37  162 |   71.80  153 |   71.79  156
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 161  Troy                    =  71.49   20  14   68.88( 225)    0   0  |    0   0  |   71.48  159 |   71.47  160 |   72.09  148
 162  Wright State            =  71.48   18  12   70.00( 180)    0   0  |    0   0  |   71.24  166 |   71.85  152 |   72.08  149
 163  DePaul                  =  71.34    9  23   78.28(  56)    0   2  |    0  14  |   71.87  152 |   70.45  178 |   69.84  186
 164  Tennessee State         =  71.33   15  13   69.21( 209)    0   1  |    0   2  |   71.34  163 |   71.28  163 |   71.14  167
 165  Ball State              =  71.30   20  12   68.93( 222)    0   0  |    0   0  |   71.03  169 |   71.71  156 |   71.99  154
 166  Pennsylvania            =  71.21   13  15   70.44( 164)    0   1  |    0   2  |   71.50  158 |   70.73  173 |   70.64  175
 167  Western Michigan        =  71.21   15  16   71.54( 134)    0   2  |    0   2  |   71.32  165 |   71.00  170 |   71.23  165
 168  Loyola Marymount        =  71.14   14  15   72.39( 121)    0   4  |    0   4  |   70.98  170 |   71.37  161 |   71.54  158
 169  Wofford                 =  70.95   13  17   71.47( 136)    0   0  |    0   2  |   71.23  167 |   70.48  177 |   70.45  179
 170  UAB                     =  70.95   16  16   69.88( 186)    0   2  |    0   2  |   71.07  168 |   70.72  174 |   70.02  183
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 171  Green Bay               =  70.87   16  13   69.39( 199)    0   1  |    0   2  |   70.66  174 |   71.17  167 |   71.24  163
 172  Washington State        =  70.86   12  18   77.33(  69)    0   5  |    0   9  |   70.60  176 |   71.25  164 |   71.39  161
 173  East Carolina           =  70.85   15  18   73.02( 105)    0   5  |    0   5  |   70.73  172 |   71.02  169 |   71.08  169
 174  Omaha(Neb.-Omaha)       =  70.84   17  14   71.12( 143)    0   1  |    0   2  |   70.57  177 |   71.24  166 |   71.53  159
 175  Weber State             =  70.69   17  13   67.59( 268)    0   0  |    0   0  |   70.65  175 |   70.74  172 |   70.69  174
 176  North Dakota            =  70.69   19   9   66.54( 301)    0   0  |    0   0  |   70.54  178 |   70.90  171 |   71.35  162
 177  Siena                   =  70.66   17  17   70.37( 165)    0   1  |    0   1  |   70.70  173 |   70.56  176 |   70.59  177
 178  Mercer                  =  70.60   13  17   71.10( 144)    0   1  |    0   2  |   70.75  171 |   70.33  181 |   70.35  182
 179  NC Central              =  70.44   22   8   61.08( 350)    0   0  |    0   0  |   70.48  179 |   70.35  180 |   70.73  172
 180  South Dakota State      =  70.32   16  16   70.52( 162)    0   1  |    0   1  |   70.24  183 |   70.43  179 |   70.53  178
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 181  Georgia Southern        =  70.27   16  14   70.16( 176)    0   0  |    0   1  |   70.01  185 |   70.65  175 |   70.84  171
 182  Lipscomb                =  70.14   17  13   67.67( 263)    0   1  |    0   1  |   70.47  180 |   69.57  189 |   69.76  188
 183  Hofstra                 =  70.11   14  17   70.29( 169)    0   1  |    0   1  |   70.17  184 |   69.99  185 |   69.89  184
 184  Samford                 =  70.04   17  15   68.68( 233)    0   2  |    0   2  |   70.25  182 |   69.68  187 |   69.74  190
 185  Indiana State           =  69.84   10  20   73.78(  95)    0   3  |    1   3  |   70.31  181 |   69.05  194 |   68.50  209
 186  Jacksonville State      =  69.82   18  14   69.12( 213)    0   0  |    0   2  |   69.68  186 |   70.01  184 |   70.73  173
 187  Canisius                =  69.64   18  15   68.90( 224)    0   1  |    0   1  |   69.65  189 |   69.60  188 |   69.75  189
 188  Eastern Washington      =  69.62   20  11   67.03( 287)    0   0  |    0   2  |   69.34  195 |   70.05  183 |   70.44  180
 189  Fordham                 =  69.60   12  19   72.91( 110)    0   0  |    2   1  |   69.46  193 |   69.80  186 |   69.83  187
 190  Denver                  =  69.56   16  14   68.83( 226)    0   0  |    0   0  |   69.57  191 |   69.51  190 |   69.65  192
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 191  New Hampshire           =  69.53   17  12   67.47( 274)    0   1  |    0   1  |   69.17  198 |   70.08  182 |   70.38  181
 192  Montana                 =  69.43   16  16   67.63( 265)    0   1  |    0   1  |   69.65  188 |   69.03  195 |   68.85  199
 193  Murray State            =  69.38   14  17   68.37( 240)    0   0  |    0   0  |   69.65  187 |   68.91  196 |   68.51  208
 194  Boston U.               =  69.36   17  14   67.84( 257)    0   0  |    0   1  |   69.40  194 |   69.28  193 |   69.25  194
 195  Texas State             =  69.32   18  13   68.08( 249)    0   0  |    0   0  |   69.32  196 |   69.28  192 |   69.85  185
 196  Gardner-Webb            =  69.27   16  14   66.80( 297)    0   1  |    0   2  |   69.47  192 |   68.91  197 |   69.03  196
 197  Utah Valley             =  69.15   12  16   69.37( 200)    0   1  |    0   2  |   69.58  190 |   68.39  209 |   68.41  211
 198  Northern Illinois       =  69.12   12  17   70.08( 177)    0   0  |    0   1  |   69.23  197 |   68.89  198 |   68.65  203
 199  Morehead State          =  68.91   12  16   70.31( 168)    0   1  |    0   1  |   69.00  199 |   68.73  200 |   68.56  206
 200  UC Davis                =  68.81   20  12   67.59( 269)    0   0  |    0   0  |   68.44  202 |   69.37  191 |   69.70  191
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 201  IUPUI                   =  68.68   12  18   70.96( 147)    0   1  |    0   3  |   68.79  200 |   68.48  206 |   68.55  207
 202  UTEP                    =  68.59   14  17   69.01( 218)    0   0  |    0   1  |   68.65  201 |   68.46  208 |   68.58  205
 203  Coastal Carolina        =  68.45   14  17   70.82( 151)    0   0  |    0   1  |   68.18  204 |   68.85  199 |   69.10  195
 204  Texas Southern          =  68.37   23  11   63.26( 341)    0   4  |    0   5  |   68.14  205 |   68.70  201 |   69.00  197
 205  Long Beach State        =  68.34   13  19   70.88( 149)    0   5  |    0   5  |   68.23  203 |   68.49  205 |   68.17  213
 206  Fairfield               =  68.25   16  14   68.72( 228)    0   0  |    0   0  |   68.06  206 |   68.54  203 |   68.68  201
 207  San Jose State          =  68.23   12  16   73.00( 107)    0   1  |    0   1  |   68.04  207 |   68.50  204 |   68.89  198
 208  New Orleans             =  68.16   17  11   66.41( 307)    0   1  |    0   2  |   67.84  212 |   68.63  202 |   69.47  193
 209  Bradley                 =  68.09   12  20   73.51(  99)    0   3  |    0   4  |   67.90  211 |   68.38  210 |   68.68  202
 210  Tennessee-Martin        =  68.04   19  12   67.69( 262)    0   1  |    0   1  |   67.75  214 |   68.48  207 |   68.83  200
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 211  Rider                   =  68.01   18  15   67.93( 254)    0   0  |    0   0  |   67.79  213 |   68.32  211 |   68.63  204
 212  Air Force               =  67.97   10  21   72.49( 119)    0   0  |    0   0  |   68.03  208 |   67.83  215 |   67.75  220
 213  UMBC                    =  67.93   16  12   66.93( 293)    0   0  |    0   1  |   68.03  209 |   67.73  217 |   68.05  214
 214  Duquesne                =  67.86   10  22   71.37( 138)    0   1  |    0   5  |   68.02  210 |   67.56  222 |   67.26  226
 215  Texas A&M-CorpusChristi =  67.85   17  11   65.38( 320)    0   2  |    0   2  |   67.63  215 |   68.17  212 |   68.43  210
 216  Mount St. Mary's        =  67.55   19  15   66.53( 304)    0   3  |    0   5  |   67.50  217 |   67.58  220 |   67.90  216
 217  Stony Brook-NY          =  67.53   18  13   66.97( 291)    0   0  |    0   1  |   67.29  222 |   67.88  214 |   68.37  212
 218  Central Michigan        =  67.47   14  16   70.28( 170)    0   0  |    0   0  |   67.11  225 |   68.01  213 |   67.96  215
 219  UNLV                    =  67.45   11  21   73.15( 103)    0   3  |    0   4  |   67.25  224 |   67.73  218 |   67.56  221
 220  Navy                    =  67.41   15  16   67.84( 258)    0   0  |    0   0  |   67.51  216 |   67.21  226 |   67.35  223
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 221  Western Kentucky        =  67.31   15  17   69.31( 203)    0   1  |    0   1  |   66.99  229 |   67.79  216 |   67.82  218
 222  Liberty                 =  67.29   16  13   66.53( 302)    0   0  |    0   2  |   67.09  226 |   67.56  221 |   67.86  217
 223  Idaho                   =  67.28   16  13   67.06( 285)    0   0  |    0   0  |   67.07  227 |   67.59  219 |   67.80  219
 224  Pacific                 =  67.22   10  22   72.71( 113)    0   6  |    0   6  |   67.27  223 |   67.11  227 |   66.90  230
 225  Eastern Illinois        =  67.19   12  15   67.61( 267)    0   0  |    0   0  |   67.36  220 |   66.89  229 |   66.74  231
 226  Columbia                =  67.18   10  16   69.10( 215)    0   0  |    0   2  |   67.39  219 |   66.80  231 |   66.41  234
 227  James Madison           =  67.15    9  23   70.87( 150)    0   0  |    0   0  |   67.42  218 |   66.66  234 |   66.34  237
 228  Stephen F. Austin       =  67.13   15  14   65.92( 314)    0   1  |    0   3  |   66.97  230 |   67.34  224 |   67.29  225
 229  Holy Cross              =  67.09   15  17   68.33( 242)    0   0  |    0   3  |   66.90  231 |   67.35  223 |   67.48  222
 230  Oregon State            =  67.08    4  27   77.37(  67)    0   5  |    1   6  |   67.31  221 |   66.66  233 |   65.88  242
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 231  Charlotte               =  66.85   12  17   70.24( 171)    0   1  |    0   3  |   66.73  233 |   67.00  228 |   66.93  229
 232  Little Rock             =  66.74   13  17   68.33( 243)    0   1  |    0   1  |   66.69  234 |   66.78  232 |   66.50  233
 233  Oral Roberts            =  66.65    6  22   72.96( 108)    0   1  |    0   3  |   66.99  228 |   66.05  240 |   65.71  244
 234  Houston Baptist         =  66.52   13  13   67.65( 264)    0   0  |    0   4  |   66.29  237 |   66.87  230 |   67.32  224
 235  Bowling Green           =  66.47   12  19   70.62( 158)    0   1  |    0   1  |   66.54  235 |   66.33  237 |   66.17  238
 236  Sam Houston State       =  66.47   17  13   65.62( 316)    0   1  |    0   2  |   65.98  243 |   67.22  225 |   67.19  227
 237  Illinois-Chicago        =  66.39   13  18   68.71( 232)    0   0  |    0   0  |   66.33  236 |   66.45  236 |   66.38  235
 238  Tulane                  =  66.34    6  25   74.91(  82)    0   5  |    0   5  |   66.73  232 |   65.66  245 |   65.36  248
 239  Kansas City(UMKC)       =  66.34   14  16   69.51( 196)    0   2  |    0   3  |   66.15  239 |   66.60  235 |   66.97  228
 240  Montana State           =  66.04   14  16   66.50( 305)    0   0  |    0   1  |   66.25  238 |   65.65  246 |   65.63  245
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 241  Hawai'i                 =  66.04   13  16   66.61( 300)    0   1  |    0   3  |   66.00  242 |   66.06  238 |   65.96  241
 242  South Alabama           =  65.93   12  18   69.21( 210)    0   0  |    0   0  |   65.85  245 |   66.03  241 |   66.02  240
 243  Cleveland State         =  65.82    8  22   70.71( 154)    0   2  |    0   2  |   66.03  240 |   65.45  248 |   65.25  251
 244  CS Fullerton            =  65.75   15  14   66.09( 313)    0   0  |    0   0  |   65.67  250 |   65.86  243 |   66.06  239
 245  Wagner                  =  65.74   15  14   64.35( 332)    0   0  |    0   0  |   65.69  249 |   65.80  244 |   65.87  243
 246  SE Missouri State(SEMO) =  65.65   13  18   68.03( 250)    0   0  |    0   1  |   66.01  241 |   65.02  255 |   65.22  252
 247  Portland                =  65.58    9  22   72.51( 118)    0   6  |    0   7  |   65.60  251 |   65.53  247 |   65.21  253
 248  Drexel                  =  65.57    8  23   70.46( 163)    0   0  |    0   0  |   65.84  247 |   65.09  253 |   64.77  257
 249  Portland State          =  65.56   12  16   66.53( 303)    0   0  |    0   0  |   65.75  248 |   65.21  252 |   65.15  255
 250  San Diego               =  65.54   12  18   71.49( 135)    0   5  |    0   5  |   65.19  257 |   66.05  239 |   66.53  232
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 251  Army                    =  65.52   12  19   67.39( 276)    0   1  |    0   1  |   65.92  244 |   64.82  257 |   64.72  258
 252  North Florida(UNF)      =  65.31   11  19   70.59( 161)    0   1  |    0   4  |   65.23  256 |   65.41  249 |   65.47  247
 253  Saint Louis             =  65.30   12  21   73.26( 101)    0   1  |    0   6  |   64.89  263 |   65.91  242 |   66.36  236
 254  Drake                   =  65.29    6  23   72.52( 117)    0   3  |    0   3  |   65.84  246 |   64.31  265 |   63.98  271
 255  Loyola-Maryland         =  65.27   14  16   67.96( 253)    0   1  |    0   2  |   65.24  255 |   65.28  250 |   65.33  249
 256  SE Louisiana            =  65.20   14  16   64.82( 329)    0   0  |    0   0  |   65.49  252 |   64.67  259 |   64.68  260
 257  CS Northridge           =  65.15   10  18   68.00( 251)    0   1  |    0   1  |   65.28  254 |   64.89  256 |   64.43  265
 258  USC Upstate             =  65.14   13  15   67.04( 286)    0   0  |    0   0  |   65.19  258 |   65.03  254 |   65.29  250
 259  Tennessee Tech          =  65.07   10  20   68.71( 231)    0   0  |    0   1  |   65.37  253 |   64.54  263 |   64.34  267
 260  Long Island U.(LIU)     =  65.06   19  12   63.85( 336)    0   0  |    0   1  |   64.92  262 |   65.26  251 |   65.54  246
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 261  Milwaukee               =  64.96   10  24   70.69( 155)    0   0  |    0   0  |   65.17  259 |   64.56  262 |   64.56  263
 262  Lamar                   =  64.90   15  14   64.95( 327)    0   0  |    0   0  |   65.08  260 |   64.58  261 |   65.15  254
 263  Louisiana-Monroe        =  64.60    7  24   69.94( 183)    0   0  |    0   1  |   64.92  261 |   64.04  271 |   63.70  273
 264  UTSA                    =  64.52   12  19   69.05( 216)    0   0  |    0   1  |   64.54  266 |   64.46  264 |   64.81  256
 265  Kennesaw State          =  64.47   12  18   67.41( 275)    0   1  |    0   1  |   64.61  264 |   64.22  268 |   64.50  264
 266  Eastern Kentucky        =  64.45   10  19   69.75( 190)    0   1  |    0   2  |   64.33  269 |   64.62  260 |   64.61  261
 267  Cornell                 =  64.40    7  21   71.09( 145)    0   0  |    0   1  |   64.60  265 |   64.03  272 |   63.92  272
 268  Saint Francis-Pa.       =  64.33   15  16   64.81( 330)    0   0  |    0   1  |   64.47  267 |   64.06  269 |   64.39  266
 269  Niagara                 =  64.27   10  23   68.50( 235)    0   0  |    0   0  |   64.39  268 |   64.04  270 |   64.28  268
 270  High Point              =  64.10   12  16   66.12( 312)    0   0  |    0   3  |   63.99  276 |   64.24  266 |   64.26  269
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 271  Miami-Ohio              =  64.08    9  21   70.31( 167)    0   0  |    0   0  |   64.25  272 |   63.76  276 |   63.50  278
 272  Colgate                 =  64.03    9  22   68.44( 237)    0   1  |    0   2  |   64.28  270 |   63.59  280 |   63.46  281
 273  South Florida           =  63.98    7  23   73.51(  98)    0   3  |    0   4  |   64.06  275 |   63.82  274 |   63.46  280
 274  Fairleigh Dickinson     =  63.95   10  19   67.07( 284)    0   1  |    0   2  |   64.07  274 |   63.70  277 |   63.40  282
 275  Brown                   =  63.91   11  17   67.58( 271)    0   1  |    0   2  |   63.82  279 |   64.03  273 |   64.16  270
 276  Florida Atlantic        =  63.90    8  20   69.52( 195)    0   0  |    0   1  |   64.08  273 |   63.58  281 |   63.52  277
 277  Pepperdine              =  63.82    8  22   72.66( 115)    0   4  |    0   4  |   63.20  286 |   64.73  258 |   64.71  259
 278  Robert Morris           =  63.81   14  19   66.97( 292)    0   1  |    0   2  |   63.91  278 |   63.63  278 |   63.66  274
 279  Appalachian State       =  63.74    7  21   70.69( 156)    0   1  |    0   1  |   63.97  277 |   63.31  283 |   63.18  285
 280  Manhattan               =  63.67   10  22   69.33( 202)    0   2  |    0   2  |   63.57  280 |   63.80  275 |   63.65  276
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 281  Fla. International      =  63.61    5  24   68.41( 238)    0   0  |    0   1  |   64.28  271 |   62.40  295 |   61.86  300
 282  Seattle                 =  63.59   10  17   67.83( 259)    0   1  |    0   1  |   63.55  281 |   63.62  279 |   63.66  275
 283  Delaware                =  63.53   11  20   71.33( 140)    0   0  |    0   1  |   63.05  287 |   64.23  267 |   64.59  262
 284  Jacksonville            =  63.43   13  15   65.23( 324)    0   0  |    0   0  |   63.42  283 |   63.41  282 |   63.48  279
 285  NJIT(New Jersey Tech)   =  63.34    9  20   68.26( 246)    0   1  |    0   2  |   63.48  282 |   63.08  286 |   62.79  289
 286  Northern Colorado       =  63.23    9  18   67.88( 256)    0   1  |    0   2  |   63.36  284 |   62.97  288 |   63.00  288
 287  Youngstown State        =  63.07   11  21   69.78( 188)    0   0  |    0   1  |   63.02  288 |   63.12  285 |   63.23  284
 288  Bryant                  =  63.06   11  20   66.27( 310)    0   2  |    0   3  |   63.22  285 |   62.78  290 |   62.68  291
 289  Cal Poly-SLO            =  62.93    9  20   68.99( 220)    0   0  |    0   0  |   62.88  289 |   62.99  287 |   63.04  287
 290  Detroit                 =  62.82    7  23   70.60( 159)    0   1  |    0   1  |   62.80  291 |   62.81  289 |   62.57  295
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 291  Austin Peay             =  62.68    9  19   69.71( 192)    0   0  |    0   3  |   62.33  294 |   63.17  284 |   63.35  283
 292  Quinnipiac              =  62.66   10  21   68.71( 230)    0   1  |    0   2  |   62.80  292 |   62.40  294 |   62.18  297
 293  UMass Lowell            =  62.56   10  20   66.22( 311)    0   0  |    0   1  |   62.87  290 |   62.01  300 |   61.80  301
 294  UC Riverside            =  62.35    6  21   68.64( 234)    0   1  |    0   2  |   62.37  293 |   62.29  297 |   62.05  298
 295  Sacramento State        =  62.28   11  18   67.19( 281)    0   0  |    0   0  |   62.18  296 |   62.41  293 |   62.59  294
 296  Campbell                =  62.22   14  17   64.96( 326)    0   1  |    0   1  |   61.96  299 |   62.60  291 |   63.07  286
 297  Radford                 =  62.10   12  18   67.58( 270)    0   2  |    0   3  |   61.79  300 |   62.55  292 |   62.71  290
 298  Dartmouth               =  62.07    7  20   69.26( 205)    0   0  |    0   1  |   62.22  295 |   61.80  302 |   61.54  302
 299  Western Illinois        =  62.07    6  20   69.92( 184)    0   1  |    0   2  |   62.10  297 |   61.97  301 |   61.98  299
 300  Norfolk State           =  61.94   15  16   63.46( 339)    0   1  |    0   3  |   61.69  301 |   62.30  296 |   62.63  292
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 301  Northwestern State      =  61.82    9  16   66.42( 306)    0   0  |    0   0  |   61.60  303 |   62.14  298 |   62.21  296
 302  American U.             =  61.79    8  22   67.56( 272)    0   1  |    0   2  |   62.06  298 |   61.30  305 |   61.00  308
 303  Alcorn State            =  61.77   15  14   62.38( 344)    0   0  |    0   0  |   61.57  304 |   62.06  299 |   62.60  293
 304  Sacred Heart            =  61.45   13  19   64.84( 328)    0   1  |    0   1  |   61.63  302 |   61.13  307 |   61.13  306
 305  Abilene Christian       =  61.44    9  16   65.72( 315)    0   0  |    0   0  |   61.44  305 |   61.41  303 |   61.46  303
 306  Binghamton-NY           =  61.17    9  20   66.99( 289)    0   0  |    0   1  |   61.06  308 |   61.31  304 |   61.21  305
 307  Hampton                 =  61.02   12  16   62.91( 343)    0   0  |    0   1  |   60.87  310 |   61.22  306 |   61.37  304
 308  Marist                  =  60.99    8  24   69.52( 194)    0   1  |    0   2  |   60.89  309 |   61.12  308 |   61.06  307
 309  Charleston Southern     =  60.92    9  19   66.28( 309)    0   1  |    0   2  |   61.09  307 |   60.58  310 |   60.49  311
 310  North Texas             =  60.86    6  22   68.19( 247)    0   0  |    0   1  |   61.13  306 |   60.36  312 |   59.88  320
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 311  Incarnate Word          =  60.64    8  17   66.73( 298)    0   0  |    0   1  |   60.73  312 |   60.47  311 |   60.67  310
 312  UC Santa Barbara        =  60.63    5  22   69.73( 191)    0   2  |    0   2  |   60.57  314 |   60.69  309 |   60.20  315
 313  SIU-Edwardsville        =  60.58    5  23   68.95( 221)    0   0  |    0   2  |   60.75  311 |   60.27  314 |   60.09  318
 314  UTRGV                   =  60.45    7  22   68.28( 245)    0   0  |    0   0  |   60.58  313 |   60.20  315 |   60.22  314
 315  The Citadel             =  60.06    9  21   69.42( 198)    0   1  |    0   2  |   59.88  318 |   60.31  313 |   60.69  309
 316  Central Arkansas        =  59.96    8  24   68.17( 248)    0   3  |    0   4  |   59.98  315 |   59.89  318 |   60.13  317
 317  Southern U.             =  59.86   13  17   61.36( 349)    0   1  |    0   1  |   59.92  316 |   59.74  319 |   59.58  322
 318  Md.-Eastern Shore(UMES) =  59.80   12  20   65.32( 322)    0   2  |    0   3  |   59.89  317 |   59.63  320 |   59.67  321
 319  Stetson                 =  59.67    8  21   67.03( 288)    0   0  |    0   0  |   59.35  320 |   60.13  316 |   60.32  313
 320  Southern Miss           =  59.50    7  22   69.11( 214)    0   1  |    0   1  |   59.07  324 |   60.11  317 |   60.37  312
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 321  Prairie View A&M        =  59.42   11  20   64.06( 333)    0   2  |    0   4  |   59.49  319 |   59.27  325 |   59.43  323
 322  Jackson State           =  59.30   12  17   61.68( 346)    0   1  |    0   1  |   59.22  321 |   59.39  323 |   59.31  326
 323  McNeese State           =  59.22    5  21   67.74( 261)    0   2  |    0   2  |   59.14  322 |   59.31  324 |   59.32  325
 324  Northern Arizona        =  59.12    8  23   66.85( 296)    0   0  |    0   0  |   59.14  323 |   59.06  327 |   59.16  329
 325  Morgan State            =  58.81   13  16   61.61( 347)    0   0  |    0   0  |   58.58  327 |   59.12  326 |   59.43  324
 326  Nicholls State          =  58.79   10  17   67.35( 277)    0   1  |    0   2  |   58.35  328 |   59.42  322 |   60.16  316
 327  VMI                     =  58.64    4  24   70.21( 172)    0   1  |    0   3  |   58.83  325 |   58.30  330 |   58.16  331
 328  Idaho State             =  58.53    4  26   69.00( 219)    0   1  |    0   2  |   58.67  326 |   58.25  331 |   57.81  332
 329  Lafayette               =  58.50    8  21   67.96( 252)    0   1  |    0   1  |   58.12  330 |   59.05  328 |   59.20  328
 330  Western Carolina        =  58.50    7  23   71.35( 139)    0   1  |    0   3  |   57.69  332 |   59.59  321 |   60.07  319
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 331  Savannah State          =  58.46   11  16   63.74( 338)    0   2  |    0   2  |   58.23  329 |   58.78  329 |   59.26  327
 332  Hartford                =  57.46    9  23   66.91( 294)    0   0  |    0   0  |   57.21  334 |   57.82  332 |   58.18  330
 333  Southern Utah           =  57.29    4  27   67.49( 273)    0   0  |    0   0  |   57.69  331 |   56.54  336 |   56.29  336
 334  Howard                  =  57.20    8  24   64.69( 331)    0   1  |    0   4  |   57.38  333 |   56.87  334 |   56.44  335
 335  SC State                =  56.72    9  20   65.42( 318)    0   2  |    0   6  |   56.49  336 |   57.04  333 |   57.03  334
 336  Grambling State         =  56.57   13  17   61.57( 348)    0   1  |    0   1  |   56.39  337 |   56.83  335 |   57.66  333
 337  Maine                   =  56.22    6  25   68.32( 244)    0   1  |    0   2  |   56.51  335 |   55.67  338 |   55.68  338
 338  Chicago State           =  56.00    3  26   71.96( 128)    0   2  |    0   3  |   56.00  338 |   55.98  337 |   56.13  337
 339  Central Connecticut St. =  55.56    6  23   65.00( 325)    0   0  |    0   1  |   55.60  340 |   55.46  339 |   55.53  339
 340  Delaware State          =  55.47    8  22   63.88( 335)    0   1  |    0   2  |   55.60  339 |   55.20  341 |   55.26  340
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 341  Alabama State           =  55.25    7  23   63.32( 340)    0   0  |    0   1  |   55.30  341 |   55.15  342 |   54.92  342
 342  Bethune-Cookman         =  55.21    8  22   61.91( 345)    0   0  |    0   0  |   55.20  342 |   55.20  340 |   55.18  341
 343  MVSU(Miss. Valley St.)  =  54.23    7  25   65.26( 323)    0   3  |    0   6  |   54.26  344 |   54.14  343 |   54.27  344
 344  St. Francis-NY          =  54.13    3  27   65.47( 317)    0   1  |    0   1  |   54.38  343 |   53.66  345 |   53.07  345
 345  Coppin State            =  53.62    7  23   65.33( 321)    0   0  |    0   2  |   53.27  346 |   54.10  344 |   54.39  343
 346  Longwood                =  53.14    4  24   66.65( 299)    0   0  |    0   2  |   53.16  347 |   53.08  346 |   52.88  346
 347  Florida A&M             =  53.00    5  23   61.06( 351)    0   1  |    0   1  |   53.29  345 |   52.46  347 |   52.45  347
 348  Ark.-Pine Bluff         =  51.98    6  24   63.99( 334)    0   1  |    0   1  |   51.88  349 |   52.11  348 |   52.28  348
 349  NC A&T                  =  51.51    1  29   63.82( 337)    0   1  |    0   1  |   52.05  348 |   50.42  350 |   49.63  350
 350  Presbyterian College    =  50.86    3  25   67.32( 279)    0   0  |    0   0  |   50.59  350 |   51.24  349 |   51.34  349
College Basketball 2016-2017          Div I games only    through games of 2017 March 12 Sunday                                                 
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 |  PREDICTOR   | GOLDEN_MEAN  |  RECENT    
                HOME ADVANTAGE=[  3.03]                                               [  3.03]       [  3.03]       [  3.03]
 351  Alabama A&M             =  48.83    2  27   63.18( 342)    0   0  |    0   0  |   48.88  351 |   48.72  351 |   48.56  351
"""
elif config.date == 2015:
    lineparts = ["Rank","Team","Rating","W","L","Schedule","ScheduleRank","WinsVsTop25","LossesVsTop25","WinsVsTop50","LossesVsTop50","ELO_SCORE","ELO_RANK","PREDICTOR","PREDICTOR_RANK"]
    text = """                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
   1  Kentucky                = 100.30   34   0   78.86(  41)    6   0  |   14   0  |   99.17    1 |   99.71    1 |  102.79    1
   2  Wisconsin               =  95.43   31   3   80.11(  15)    7   1  |   12   2  |   95.42    2 |   95.60    2 |   94.93    5
   3  Virginia                =  94.93   29   3   78.98(  37)    3   3  |    9   3  |   94.52    3 |   94.42    4 |   95.69    4
   4  Arizona                 =  94.55   31   3   77.86(  58)    3   0  |   11   0  |   94.39    4 |   94.71    3 |   94.19    7
   5  Duke                    =  94.46   29   4   80.11(  16)    7   2  |   10   4  |   93.88    6 |   93.76    5 |   95.82    3
   6  Villanova               =  94.41   32   2   79.06(  34)    3   1  |   13   1  |   94.23    5 |   93.35    6 |   95.97    2
   7  Gonzaga                 =  93.28   31   2   75.64(  87)    0   1  |    6   2  |   93.01    7 |   92.44    7 |   94.42    6
   8  Notre Dame              =  89.92   29   5   77.81(  60)    6   2  |   10   3  |   88.80   14 |   88.99   15 |   92.70    8
   9  North Carolina          =  89.92   24  11   82.10(   2)    4   9  |    9  10  |   90.74    9 |   90.94    9 |   88.18   14
  10  Kansas                  =  89.89   26   8   83.13(   1)   11   5  |   13   6  |   89.89   11 |   89.13   14 |   90.55    9
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
  11  Iowa State              =  89.88   25   8   81.85(   4)   11   4  |   13   5  |   90.30   10 |   89.34   13 |   89.84   10
  12  Utah                    =  89.67   23   8   78.11(  52)    1   3  |    5   7  |   91.29    8 |   91.99    8 |   86.95   18
  13  Oklahoma                =  89.14   22  10   81.94(   3)    7   6  |   11   6  |   88.64   15 |   90.17   10 |   88.28   13
  14  Baylor                  =  88.92   23   9   81.49(   7)    7   5  |    8   8  |   88.92   13 |   89.37   12 |   88.12   16
  15  Louisville              =  88.42   24   8   79.77(  23)    3   6  |    6   7  |   87.98   17 |   88.72   16 |   88.15   15
  16  Michigan State          =  87.74   23  11   79.83(  21)    3   5  |    8   8  |   88.53   16 |   87.89   17 |   86.65   20
  17  Ohio State              =  87.48   23  10   77.90(  56)    0   7  |    4   9  |   89.04   12 |   89.91   11 |   84.57   28
  18  Wichita State           =  87.37   27   4   74.01( 116)    1   2  |    1   2  |   86.74   21 |   87.28   19 |   87.75   17
  19  West Virginia           =  87.01   23   9   80.01(  18)    3   8  |    6   9  |   87.68   19 |   86.48   21 |   86.73   19
  20  Butler                  =  86.82   22  10   79.95(  20)    2   5  |    6   9  |   87.56   20 |   86.92   20 |   85.79   24
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
  21  Texas                   =  86.65   20  13   80.66(  11)    3  10  |    3  13  |   87.79   18 |   87.66   18 |   84.66   27
  22  Northern Iowa           =  85.89   30   3   73.18( 136)    2   1  |    3   2  |   84.07   34 |   85.08   25 |   89.57   11
  23  Georgetown              =  85.85   21  10   80.73(  10)    3   4  |    6  10  |   85.40   25 |   86.00   23 |   85.75   25
  24  Iowa                    =  85.61   21  11   79.57(  25)    3   6  |    6   7  |   86.05   22 |   86.18   22 |   84.35   34
  25  Arkansas                =  85.61   26   8   77.24(  68)    0   3  |    4   5  |   85.28   27 |   85.02   26 |   86.35   21
  26  Xavier-Ohio             =  85.50   21  13   80.28(  14)    5   4  |    8   7  |   85.96   23 |   85.76   24 |   84.50   30
  27  Maryland                =  85.48   27   6   78.63(  46)    4   4  |    8   6  |   84.31   30 |   84.30   32 |   88.64   12
  28  Providence              =  85.44   22  11   80.58(  12)    4   5  |    7   8  |   85.36   26 |   84.61   28 |   86.27   22
  29  SMU                     =  85.01   26   6   74.97(  95)    0   2  |    0   5  |   84.15   31 |   84.50   29 |   86.26   23
  30  Davidson                =  84.63   23   7   74.92(  99)    0   2  |    2   4  |   84.75   29 |   84.38   30 |   84.46   33
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
  31  VCU(Va. Commonwealth)   =  84.32   26   9   77.54(  66)    1   2  |    6   4  |   83.22   40 |   83.95   36 |   85.68   26
  32  NC State                =  84.15   20  13   79.67(  24)    3   6  |    4   9  |   85.10   28 |   84.16   34 |   83.05   38
  33  Purdue                  =  84.10   21  12   78.98(  38)    2   5  |    7   7  |   85.68   24 |   83.85   37 |   82.86   40
  34  Oklahoma State          =  84.01   17  13   81.51(   6)    5   8  |    5   9  |   84.10   33 |   84.30   31 |   83.25   37
  35  San Diego State         =  83.86   25   8   75.09(  92)    1   1  |    2   4  |   83.32   39 |   84.09   35 |   83.76   35
  36  BYU                     =  83.85   23   9   76.06(  82)    1   3  |    2   5  |   83.92   35 |   84.80   27 |   82.49   43
  37  Georgia                 =  83.38   21  11   79.06(  35)    0   5  |    1   6  |   82.94   41 |   83.39   38 |   83.42   36
  38  St. John's              =  83.36   20  11   79.96(  19)    1   7  |    5   8  |   82.90   42 |   82.60   46 |   84.50   31
  39  Miami-Florida           =  83.22   21  12   78.06(  53)    1   6  |    4   7  |   84.14   32 |   83.20   40 |   82.15   47
  40  Indiana                 =  83.04   20  13   78.82(  43)    2   7  |    5  11  |   83.37   38 |   83.06   41 |   82.38   45
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
  41  Stephen F. Austin       =  82.61   26   4   68.93( 290)    0   2  |    0   3  |   81.49   55 |   81.87   53 |   84.55   29
  42  Florida                 =  82.53   16  17   80.28(  13)    1   6  |    1  10  |   83.77   36 |   84.17   33 |   79.83   66
  43  LSU                     =  82.45   22  10   76.71(  77)    2   1  |    5   1  |   82.34   47 |   82.07   50 |   82.67   41
  44  Oregon                  =  82.44   24   9   77.75(  61)    2   3  |    5   5  |   81.75   52 |   81.30   56 |   84.49   32
  45  Boise State             =  82.41   23   8   73.62( 126)    0   1  |    2   2  |   81.85   51 |   82.58   47 |   82.39   44
  46  Illinois                =  82.34   19  13   78.39(  50)    2   5  |    4   9  |   82.31   48 |   83.31   39 |   81.01   54
  47  UCLA                    =  82.19   20  13   78.52(  48)    1   7  |    4   8  |   82.39   45 |   81.75   55 |   82.19   46
  48  Dayton                  =  82.13   25   8   74.97(  96)    0   1  |    1   3  |   81.13   56 |   82.01   51 |   82.94   39
  49  Stanford                =  82.12   19  13   77.99(  55)    1   5  |    1   9  |   81.89   50 |   82.75   43 |   81.29   51
  50  Cincinnati              =  82.07   22  10   75.02(  94)    0   0  |    4   2  |   82.38   46 |   82.00   52 |   81.51   49
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
  51  Mississippi             =  82.03   20  12   77.66(  65)    1   2  |    5   7  |   81.65   53 |   82.69   44 |   81.30   50
  52  TCU                     =  82.00   18  15   78.43(  49)    0  13  |    1  14  |   82.82   43 |   82.38   48 |   80.57   62
  53  Syracuse                =  81.97   18  13   78.54(  47)    3   5  |    3   8  |   82.10   49 |   82.67   45 |   80.78   57
  54  Minnesota               =  81.96   17  15   78.80(  44)    2   6  |    5  10  |   83.41   37 |   82.80   42 |   79.70   68
  55  Texas A&M               =  81.66   20  11   77.07(  70)    0   3  |    3   6  |   81.56   54 |   81.82   54 |   81.22   53
  56  Vanderbilt              =  81.45   18  13   76.93(  74)    0   3  |    2   7  |   82.43   44 |   82.23   49 |   79.53   73
  57  Colorado State          =  81.43   26   6   73.08( 138)    0   0  |    2   3  |   80.97   58 |   80.65   61 |   82.58   42
  58  Rhode Island            =  80.92   21   9   74.46( 107)    0   1  |    0   6  |   80.43   63 |   81.09   58 |   80.81   56
  59  Buffalo                 =  80.88   23   9   73.97( 118)    0   2  |    0   2  |   80.73   61 |   80.89   59 |   80.66   59
  60  Saint Mary's-Cal.       =  80.83   20   9   74.94(  98)    0   2  |    1   5  |   81.13   57 |   80.50   62 |   80.59   61
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
  61  Alabama                 =  80.64   17  14   78.66(  45)    0   5  |    1  10  |   80.83   59 |   80.89   60 |   79.83   65
  62  Old Dominion            =  80.48   24   7   71.69( 176)    0   0  |    2   0  |   80.76   60 |   80.41   64 |   79.94   64
  63  Richmond                =  80.10   19  13   75.83(  85)    0   1  |    3   5  |   79.81   64 |   80.49   63 |   79.57   71
  64  South Carolina          =  80.07   16  16   79.17(  32)    1   5  |    4   8  |   79.58   68 |   81.26   57 |   78.88   82
  65  Michigan                =  79.97   15  16   80.78(   9)    1   8  |    4  13  |   79.78   65 |   79.95   66 |   79.79   67
  66  Tulsa                   =  79.92   22   9   74.39( 108)    0   2  |    0   6  |   79.34   70 |   79.34   71 |   80.88   55
  67  Valparaiso              =  79.85   25   5   70.91( 196)    0   0  |    0   0  |   78.94   77 |   79.22   72 |   81.27   52
  68  Temple                  =  79.76   23  10   74.89( 100)    1   2  |    2   6  |   78.37   85 |   79.15   75 |   81.76   48
  69  George Washington       =  79.74   21  12   75.17(  90)    1   1  |    2   5  |   79.46   69 |   79.91   67 |   79.43   76
  70  Arizona State           =  79.72   17  15   77.52(  67)    1   3  |    3   7  |   79.61   66 |   80.19   65 |   78.93   81
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
  71  Connecticut             =  79.68   20  14   75.96(  83)    0   3  |    5   7  |   79.15   72 |   79.89   68 |   79.56   72
  72  Murray State            =  79.63   25   5   69.77( 246)    0   0  |    0   1  |   78.87   78 |   79.06   77 |   80.77   58
  73  Seton Hall              =  79.61   16  15   79.14(  33)    1   6  |    3  11  |   80.58   62 |   78.88   78 |   79.27   79
  74  Kansas State            =  79.55   15  17   81.64(   5)    5   8  |    7  10  |   79.60   67 |   79.11   76 |   79.68   69
  75  Green Bay               =  79.47   22   8   72.17( 163)    0   1  |    1   1  |   78.95   76 |   79.19   74 |   79.95   63
  76  Pittsburgh              =  79.44   18  14   78.30(  51)    2   4  |    2   9  |   78.79   79 |   79.58   70 |   79.53   74
  77  Illinois State          =  79.40   20  12   74.58( 105)    1   5  |    1   6  |   78.54   82 |   79.72   69 |   79.48   75
  78  Georgia State           =  78.94   23   9   70.61( 207)    0   1  |    0   1  |   79.10   75 |   79.19   73 |   78.13   89
  79  Louisiana Tech          =  78.94   24   8   71.00( 192)    0   0  |    0   1  |   78.47   84 |   78.69   80 |   79.33   77
  80  Central Michigan        =  78.92   20   8   71.96( 165)    0   0  |    0   0  |   79.23   71 |   78.65   81 |   78.60   83
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
  81  Penn State              =  78.76   18  16   77.89(  57)    1   6  |    1  12  |   79.12   73 |   78.80   79 |   78.02   90
  82  Creighton               =  78.30   14  19   79.47(  26)    1   7  |    3  11  |   79.11   74 |   78.28   83 |   77.25   98
  83  Clemson                 =  78.28   16  15   78.05(  54)    1   6  |    3   8  |   77.84   93 |   78.19   84 |   78.44   86
  84  Memphis                 =  78.26   18  14   74.39( 109)    0   3  |    1   8  |   78.76   80 |   78.53   82 |   77.15  101
  85  Harvard                 =  78.24   20   7   71.97( 164)    0   1  |    0   1  |   77.83   94 |   77.43   93 |   79.32   78
  86  Tennessee               =  78.17   16  16   79.28(  30)    2   4  |    3   9  |   77.88   92 |   77.85   86 |   78.48   85
  87  Yale                    =  78.01   20  10   73.11( 137)    0   0  |    0   2  |   77.81   95 |   77.62   90 |   78.32   87
  88  Colorado                =  78.00   15  17   77.84(  59)    0   4  |    2   8  |   78.04   87 |   78.17   85 |   77.39   94
  89  Marquette               =  77.91   13  19   80.83(   8)    0  10  |    1  15  |   78.64   81 |   77.61   91 |   77.25   99
  90  Florida State           =  77.83   17  16   77.73(  63)    0   6  |    2   9  |   78.50   83 |   77.13   98 |   77.72   91
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
  91  Toledo                  =  77.82   20  13   73.69( 124)    0   1  |    0   3  |   77.98   88 |   77.80   87 |   77.31   96
  92  Wofford                 =  77.57   26   6   69.46( 264)    0   2  |    1   3  |   76.10  116 |   76.29  114 |   80.65   60
  93  UTEP                    =  77.47   22  10   71.79( 174)    0   1  |    1   1  |   76.79  105 |   77.73   89 |   77.45   93
  94  Sam Houston State       =  77.34   21   8   68.00( 324)    0   0  |    0   4  |   76.99  102 |   77.29   95 |   77.36   95
  95  Bowling Green           =  77.34   20  10   71.87( 170)    0   0  |    0   1  |   77.62   97 |   77.09   99 |   77.00  103
  96  Northwestern            =  77.33   15  17   78.82(  42)    1   8  |    2  13  |   77.79   96 |   77.03  100 |   76.89  104
  97  UC Irvine               =  77.20   19  12   72.95( 142)    0   1  |    0   2  |   78.20   86 |   76.60  110 |   76.67  107
  98  Wyoming                 =  77.18   23   9   72.38( 158)    0   0  |    3   3  |   75.41  124 |   76.51  111 |   79.63   70
  99  Georgia Tech            =  77.11   12  19   79.28(  29)    0   7  |    2   9  |   77.37   99 |   77.76   88 |   75.77  119
 100  Iona                    =  77.11   26   8   70.60( 209)    0   1  |    0   1  |   75.94  119 |   76.88  104 |   78.22   88
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 101  UC Santa Barbara        =  77.11   17  13   73.97( 117)    0   1  |    0   3  |   77.97   89 |   76.90  103 |   76.21  114
 102  Pepperdine              =  77.09   17  13   74.73( 102)    0   4  |    2   4  |   77.61   98 |   76.92  102 |   76.46  111
 103  California              =  77.06   18  15   77.04(  72)    0   6  |    1  10  |   76.55  109 |   76.05  115 |   78.53   84
 104  UNLV                    =  77.02   17  15   75.26(  89)    1   2  |    1   8  |   76.84  104 |   77.30   94 |   76.50  108
 105  Nebraska                =  76.94   13  18   79.27(  31)    1   5  |    3  10  |   77.90   91 |   76.66  107 |   76.05  116
 106  New Mexico State        =  76.84   21  10   68.22( 317)    0   2  |    0   2  |   77.92   90 |   77.20   97 |   75.11  128
 107  La Salle                =  76.80   17  16   75.83(  86)    0   2  |    2   5  |   77.00  101 |   76.77  105 |   76.29  113
 108  UC Davis                =  76.76   23   6   70.84( 198)    0   0  |    0   0  |   75.53  122 |   75.80  119 |   78.97   80
 109  Washington              =  76.74   16  15   76.72(  76)    2   2  |    4   7  |   75.95  118 |   76.64  109 |   77.29   97
 110  Oregon State            =  76.67   16  14   76.78(  75)    1   2  |    2   7  |   75.42  123 |   76.64  108 |   77.58   92
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 111  St. Bonaventure         =  76.61   18  13   73.47( 130)    0   0  |    2   3  |   77.31  100 |   75.99  116 |   76.36  112
 112  Boston College          =  76.58   13  19   79.37(  28)    0   8  |    2  11  |   76.33  113 |   76.92  101 |   76.04  117
 113  Akron                   =  76.51   20  14   72.89( 145)    0   0  |    0   1  |   76.59  108 |   76.40  112 |   76.20  115
 114  San Diego               =  76.38   14  16   76.29(  81)    0   2  |    1   7  |   76.42  111 |   77.29   96 |   74.93  132
 115  William & Mary          =  76.36   18  12   71.87( 172)    0   1  |    0   2  |   76.94  103 |   76.38  113 |   75.43  122
 116  Massachusetts           =  76.30   17  15   76.55(  78)    0   1  |    1   6  |   76.13  115 |   75.42  125 |   77.21  100
 117  South Dakota State      =  76.26   21  10   69.18( 279)    0   2  |    0   2  |   76.76  106 |   76.76  106 |   74.87  135
 118  NC Central              =  76.22   22   7   65.03( 349)    0   1  |    0   3  |   76.09  117 |   75.80  118 |   76.48  110
 119  Hofstra                 =  75.94   20  13   69.31( 270)    0   0  |    0   1  |   76.62  107 |   77.59   92 |   73.13  157
 120  Kent State              =  75.88   20  11   72.55( 153)    0   1  |    0   1  |   75.61  121 |   75.30  126 |   76.49  109
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 121  Wake Forest             =  75.82   13  19   79.05(  36)    0   8  |    2  10  |   76.23  114 |   75.67  121 |   75.24  126
 122  Portland                =  75.73   15  15   75.07(  93)    0   2  |    0   5  |   76.42  112 |   75.72  120 |   74.73  136
 123  Northeastern            =  75.70   23  11   71.53( 180)    0   0  |    0   0  |   75.01  129 |   75.16  127 |   76.67  106
 124  Eastern Washington      =  75.32   23   8   69.29( 272)    0   0  |    1   1  |   74.61  133 |   74.24  141 |   77.06  102
 125  Cleveland State         =  75.30   16  14   72.54( 154)    0   2  |    0   3  |   75.18  125 |   75.85  117 |   74.38  142
 126  Hawai'i                 =  75.27   20  13   71.79( 173)    0   1  |    0   2  |   75.61  120 |   74.86  130 |   75.07  130
 127  Evansville              =  75.11   18  12   72.37( 159)    1   3  |    1   3  |   74.60  135 |   74.59  133 |   75.88  118
 128  Utah State              =  75.09   17  13   72.98( 140)    0   0  |    1   3  |   74.16  140 |   75.45  123 |   75.17  127
 129  Eastern Michigan        =  75.07   17  13   72.94( 143)    0   1  |    0   2  |   74.89  131 |   75.07  129 |   74.89  134
 130  Albany-NY               =  75.02   24   8   68.46( 311)    0   0  |    0   1  |   74.58  136 |   73.64  145 |   76.86  105
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 131  DePaul                  =  75.01   12  20   78.88(  40)    0   6  |    3  10  |   76.49  110 |   74.34  137 |   74.09  145
 132  Loyola-Chicago          =  74.89   17  13   73.25( 134)    0   6  |    1   6  |   74.60  134 |   74.40  135 |   75.41  123
 133  Stony Brook-NY          =  74.85   21  11   70.07( 231)    0   0  |    0   3  |   75.11  127 |   74.27  140 |   74.94  131
 134  Texas Tech              =  74.84   13  19   79.47(  27)    1  12  |    2  14  |   75.01  128 |   74.35  136 |   74.90  133
 135  Long Beach State        =  74.64   14  17   77.11(  69)    0   2  |    1   8  |   73.86  143 |   74.60  132 |   75.08  129
 136  Western Michigan        =  74.60   18  13   73.72( 123)    0   0  |    0   0  |   74.03  142 |   74.01  142 |   75.53  121
 137  San Francisco           =  74.56   13  18   74.97(  97)    0   3  |    0   5  |   75.16  126 |   75.43  124 |   72.60  163
 138  Auburn                  =  74.55   14  20   78.89(  39)    0   3  |    4   6  |   73.68  146 |   74.31  138 |   75.32  125
 139  New Mexico              =  74.48   15  16   73.88( 120)    0   0  |    0   4  |   74.38  137 |   75.13  128 |   73.42  150
 140  Western Kentucky        =  74.44   18  12   72.36( 160)    0   1  |    0   1  |   73.76  145 |   73.91  143 |   75.40  124
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 141  Vermont                 =  74.30   17  13   68.62( 306)    0   0  |    0   0  |   74.89  130 |   75.54  122 |   71.88  178
 142  Louisiana-Lafayette     =  74.19   17  13   70.05( 232)    0   0  |    0   0  |   74.88  132 |   74.54  134 |   72.73  162
 143  North Florida(UNF)      =  73.94   20  11   67.75( 326)    0   2  |    1   2  |   74.14  141 |   73.60  146 |   73.81  148
 144  UAB                     =  73.93   18  15   72.58( 150)    0   2  |    0   5  |   73.30  149 |   73.82  144 |   74.29  143
 145  Coastal Carolina        =  73.88   20   9   67.33( 334)    0   0  |    0   1  |   73.57  147 |   73.18  152 |   74.69  138
 146  Charlotte               =  73.85   14  18   73.51( 127)    0   1  |    0   4  |   74.32  139 |   74.61  131 |   72.09  174
 147  Georgia Southern        =  73.77   19   9   69.08( 281)    0   0  |    0   1  |   73.19  151 |   73.40  147 |   74.42  141
 148  Eastern Kentucky        =  73.75   17  11   68.96( 289)    0   1  |    1   2  |   73.35  148 |   74.28  139 |   73.11  158
 149  Southern California     =  73.69   12  20   77.02(  73)    0   3  |    0  10  |   74.34  138 |   73.19  151 |   73.32  152
 150  Belmont                 =  73.60   21  10   69.52( 261)    0   1  |    0   2  |   72.74  157 |   73.27  150 |   74.47  140
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 151  Mississippi State       =  73.40   12  19   76.47(  79)    0   3  |    1   5  |   73.79  144 |   73.32  149 |   72.76  160
 152  Middle Tennessee        =  73.22   18  16   72.77( 147)    0   0  |    0   2  |   72.51  159 |   73.33  148 |   73.40  151
 153  High Point              =  73.08   19   9   69.63( 255)    0   1  |    0   1  |   71.61  172 |   71.91  166 |   75.63  120
 154  North Dakota State      =  72.86   21   9   69.03( 282)    0   2  |    0   2  |   71.95  167 |   71.80  167 |   74.70  137
 155  Oakland-Mich.           =  72.83   14  16   74.32( 112)    0   3  |    0   4  |   72.67  158 |   72.45  158 |   73.09  159
 156  Florida Gulf Coast      =  72.75   19  10   68.49( 309)    0   0  |    0   1  |   72.28  162 |   71.96  164 |   73.82  147
 157  Cal Poly-SLO            =  72.62   11  16   74.25( 113)    0   1  |    0   1  |   72.80  156 |   72.86  155 |   71.79  184
 158  Chattanooga             =  72.59   20  10   68.77( 297)    0   2  |    0   3  |   71.76  168 |   71.79  168 |   74.01  146
 159  Manhattan               =  72.58   19  13   70.10( 229)    0   0  |    0   0  |   72.16  164 |   72.48  156 |   72.74  161
 160  USC Upstate             =  72.56   19  11   66.30( 344)    0   0  |    0   1  |   73.28  150 |   72.29  162 |   71.82  182
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 161  Washington State        =  72.55   13  18   77.73(  64)    0   4  |    2   7  |   71.67  171 |   71.39  178 |   74.48  139
 162  St. Francis-NY          =  72.53   22  11   67.37( 333)    0   1  |    0   1  |   72.40  161 |   71.79  169 |   73.19  155
 163  Montana                 =  72.51   18  12   69.39( 266)    0   0  |    0   2  |   72.41  160 |   72.32  161 |   72.47  166
 164  Canisius                =  72.47   16  14   70.41( 219)    0   0  |    0   0  |   72.99  154 |   72.47  157 |   71.61  187
 165  Rider                   =  72.47   21  11   69.81( 243)    0   2  |    0   2  |   71.00  183 |   71.95  165 |   74.15  144
 166  Columbia                =  72.44   12  15   71.48( 182)    0   1  |    0   1  |   73.19  152 |   73.09  153 |   70.51  206
 167  Virginia Tech           =  72.23   11  22   77.74(  62)    0   8  |    0  12  |   73.01  153 |   72.44  159 |   70.81  204
 168  Saint Joseph's-Pa.      =  72.20   13  18   74.66( 104)    0   2  |    1   4  |   72.06  165 |   72.06  163 |   72.12  173
 169  Princeton               =  72.15   15  14   71.02( 191)    0   0  |    0   0  |   71.72  169 |   72.35  160 |   71.94  176
 170  Morehead State          =  72.14   15  17   70.40( 220)    0   1  |    0   2  |   72.84  155 |   72.93  154 |   70.07  212
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 171  NJIT(New Jersey Tech)   =  71.97   15  11   69.92( 237)    0   1  |    0   2  |   71.51  174 |   70.93  185 |   73.32  153
 172  NC Wilmington           =  71.96   17  13   71.18( 186)    0   1  |    0   2  |   71.42  176 |   71.68  170 |   72.45  167
 173  Rutgers                 =  71.92   10  22   79.81(  22)    1   4  |    1  11  |   71.99  166 |   71.21  179 |   72.34  169
 174  Indiana State           =  71.87   14  16   72.96( 141)    0   5  |    0   6  |   72.17  163 |   71.46  175 |   71.72  186
 175  Santa Clara             =  71.80   12  18   75.88(  84)    0   3  |    0   6  |   71.34  180 |   71.56  173 |   72.16  172
 176  Lafayette               =  71.76   19  12   69.75( 247)    0   2  |    0   2  |   70.49  190 |   70.82  187 |   73.78  149
 177  Louisiana-Monroe        =  71.67   17  12   70.36( 221)    0   0  |    0   1  |   71.35  179 |   71.03  183 |   72.38  168
 178  Missouri                =  71.52    8  23   80.03(  17)    0   6  |    2  11  |   71.51  173 |   71.68  171 |   70.95  201
 179  Northern Illinois       =  71.38   13  16   73.63( 125)    0   2  |    0   2  |   70.38  192 |   71.48  174 |   71.85  180
 180  Tennessee-Martin        =  71.32   16  12   69.62( 256)    0   1  |    0   1  |   71.08  182 |   71.13  181 |   71.41  188
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 181  Colgate                 =  71.23   15  17   70.51( 215)    0   1  |    0   1  |   71.42  175 |   71.04  182 |   70.91  202
 182  Detroit                 =  71.23   13  18   73.31( 132)    0   1  |    0   2  |   71.36  178 |   70.96  184 |   71.05  200
 183  Robert Morris           =  71.21   19  14   69.02( 283)    0   2  |    0   2  |   70.92  186 |   70.44  194 |   72.06  175
 184  Monmouth-NJ             =  71.21   18  15   70.03( 233)    0   1  |    0   3  |   70.67  189 |   71.18  180 |   71.39  190
 185  American U.             =  71.14   17  16   71.15( 188)    0   0  |    0   1  |   70.05  197 |   70.86  186 |   72.16  171
 186  Mercer                  =  71.12   16  15   69.32( 269)    0   0  |    0   1  |   71.38  177 |   71.42  176 |   70.10  210
 187  Dartmouth               =  71.09   14  14   70.99( 193)    0   0  |    0   0  |   69.87  199 |   71.56  172 |   71.30  191
 188  Radford                 =  71.02   18  11   68.61( 307)    0   1  |    0   1  |   69.76  200 |   69.90  205 |   73.18  156
 189  Quinnipiac              =  70.95   15  15   69.37( 267)    0   0  |    0   0  |   71.14  181 |   71.41  177 |   69.78  218
 190  James Madison           =  70.94   19  13   70.74( 201)    0   2  |    0   2  |   69.61  204 |   70.32  197 |   72.59  164
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 191  New Hampshire           =  70.93   17  13   68.67( 301)    0   0  |    0   0  |   70.68  188 |   70.62  191 |   71.18  195
 192  Fort Wayne(IPFW)        =  70.89   13  14   70.13( 228)    0   0  |    0   1  |   71.68  170 |   70.24  198 |   70.54  205
 193  Norfolk State           =  70.78   18  13   67.62( 328)    0   2  |    0   3  |   70.98  184 |   69.97  202 |   71.20  193
 194  Bucknell                =  70.75   18  14   70.42( 218)    0   1  |    0   1  |   69.70  201 |   69.75  207 |   72.58  165
 195  Fresno State            =  70.71   13  17   74.38( 110)    0   0  |    2   2  |   69.49  206 |   70.41  195 |   71.87  179
 196  Lehigh                  =  70.71   15  14   70.20( 225)    0   1  |    0   1  |   70.09  195 |   70.49  193 |   71.20  192
 197  Northwestern State      =  70.66   15  12   69.53( 260)    0   2  |    0   5  |   69.90  198 |   69.97  203 |   71.83  181
 198  Northern Arizona        =  70.57   18  14   69.34( 268)    0   0  |    0   1  |   70.24  193 |   70.12  199 |   71.07  198
 199  Air Force               =  70.55   12  17   72.90( 144)    0   0  |    0   5  |   70.44  191 |   70.75  188 |   70.03  214
 200  Texas-Arlington         =  70.48   15  15   70.18( 227)    0   2  |    0   2  |   70.74  187 |   70.33  196 |   70.03  213
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 201  Charleston Southern     =  70.45   16  11   68.48( 310)    0   0  |    0   1  |   69.33  210 |   69.47  210 |   72.31  170
 202  George Mason            =  70.32    8  22   76.46(  80)    0   3  |    0   8  |   70.94  185 |   70.62  192 |   68.93  232
 203  Winthrop                =  70.31   16  13   67.43( 331)    0   0  |    0   1  |   69.36  208 |   70.74  189 |   70.31  209
 204  Texas Southern          =  70.28   22  12   66.91( 337)    1   2  |    1   5  |   68.87  224 |   68.54  226 |   73.27  154
 205  Incarnate Word          =  70.23   14  10   68.40( 313)    0   0  |    0   2  |   69.14  217 |   69.39  212 |   71.90  177
 206  Saint Peter's           =  70.20   16  18   69.84( 241)    0   0  |    0   0  |   70.12  194 |   70.69  190 |   69.25  227
 207  Oral Roberts            =  70.18   16  14   71.26( 184)    0   1  |    0   1  |   69.29  212 |   69.23  217 |   71.80  183
 208  Sacramento State        =  70.13   18  11   68.02( 322)    0   1  |    0   1  |   69.55  205 |   69.23  218 |   71.39  189
 209  Tulane                  =  70.05   14  16   72.67( 149)    0   0  |    1   3  |   68.83  226 |   69.81  206 |   71.12  196
 210  Gardner-Webb            =  70.01   16  14   70.59( 210)    0   1  |    1   2  |   69.15  216 |   68.89  220 |   71.78  185
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 211  Duquesne                =  69.75   11  19   74.12( 114)    0   0  |    1   4  |   69.41  207 |   69.44  211 |   70.08  211
 212  Texas-San Antonio(UTSA) =  69.72   12  16   70.81( 199)    0   0  |    0   0  |   69.16  214 |   70.04  201 |   69.48  225
 213  East Tennessee State(ETS=  69.72   14  14   70.00( 234)    0   0  |    0   1  |   69.63  203 |   69.29  216 |   69.96  215
 214  Cornell                 =  69.66   12  17   71.64( 177)    0   0  |    0   0  |   69.09  218 |   69.90  204 |   69.53  223
 215  Eastern Illinois        =  69.60   15  14   71.08( 189)    0   0  |    0   1  |   69.33  209 |   68.21  235 |   71.11  197
 216  Rice                    =  69.55   10  19   72.40( 157)    0   1  |    0   1  |   69.69  202 |   70.10  200 |   68.30  238
 217  South Dakota            =  69.53   15  16   70.25( 224)    0   0  |    0   1  |   70.06  196 |   68.65  223 |   69.70  219
 218  Saint Francis-Pa.       =  69.46   15  15   69.92( 238)    0   1  |    0   2  |   68.60  230 |   68.49  230 |   71.07  199
 219  Houston                 =  69.45   13  19   71.93( 166)    0   0  |    0   5  |   68.95  222 |   69.71  208 |   69.24  228
 220  East Carolina           =  69.44   12  19   73.48( 129)    0   1  |    1   4  |   68.73  228 |   69.30  214 |   69.91  216
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 221  Miami-Ohio              =  69.41   12  19   73.28( 133)    0   1  |    0   2  |   69.08  220 |   69.30  213 |   69.49  224
 222  Milwaukee               =  69.40   12  16   73.20( 135)    0   2  |    0   3  |   68.21  232 |   68.78  222 |   70.87  203
 223  Pacific                 =  69.35    9  19   75.54(  88)    0   2  |    0   4  |   69.24  213 |   69.30  215 |   69.15  229
 224  Fordham                 =  69.29    9  21   75.12(  91)    0   0  |    0   7  |   68.95  221 |   69.69  209 |   68.73  236
 225  Mount St. Mary's        =  69.20   15  15   69.40( 265)    0   2  |    0   2  |   69.16  215 |   67.87  239 |   70.45  207
 226  Md.-Eastern Shore(UMES) =  69.19   18  14   68.23( 316)    0   1  |    0   2  |   67.43  244 |   68.54  227 |   71.18  194
 227  UC Riverside            =  69.01   12  17   72.35( 161)    0   1  |    0   3  |   68.72  229 |   68.49  229 |   69.53  221
 228  Denver                  =  68.98   12  18   70.34( 223)    0   1  |    0   2  |   69.33  211 |   68.99  219 |   68.25  239
 229  Texas A&M-CorpusChristi =  68.94   17  13   67.56( 329)    0   1  |    1   2  |   68.46  231 |   68.60  225 |   69.43  226
 230  North Texas             =  68.88   12  17   72.41( 156)    0   1  |    0   3  |   68.85  225 |   68.01  237 |   69.58  220
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 231  Boston U.               =  68.87   12  17   70.60( 208)    0   1  |    0   2  |   68.75  227 |   68.54  228 |   69.02  231
 232  Bryant                  =  68.73   16  15   69.70( 251)    0   0  |    0   0  |   67.67  238 |   67.86  240 |   70.38  208
 233  Ohio                    =  68.59   10  20   74.09( 115)    0   0  |    0   0  |   67.57  241 |   68.62  224 |   69.13  230
 234  Southern Illinois       =  68.47   11  21   71.92( 167)    0   5  |    0   5  |   69.08  219 |   68.84  221 |   66.95  258
 235  Western Carolina        =  68.47   13  17   70.63( 205)    0   0  |    0   0  |   67.77  237 |   68.42  232 |   68.83  233
 236  Holy Cross              =  68.33   13  16   70.50( 216)    0   0  |    0   0  |   67.23  247 |   67.62  243 |   69.83  217
 237  Loyola Marymount        =  68.24    7  23   77.06(  71)    0   3  |    0   7  |   68.93  223 |   67.77  241 |   67.74  246
 238  Idaho                   =  67.96   11  17   69.47( 263)    0   0  |    0   1  |   68.03  234 |   68.44  231 |   66.86  259
 239  Texas State             =  67.90   11  17   70.35( 222)    0   1  |    0   2  |   67.58  240 |   68.27  234 |   67.34  249
 240  Army                    =  67.88   14  15   68.83( 295)    0   1  |    0   1  |   67.03  252 |   67.49  245 |   68.78  235
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 241  Missouri State          =  67.84    9  20   73.78( 122)    0   4  |    0   4  |   67.94  236 |   67.26  250 |   68.07  241
 242  Ark.-Little Rock(UALR)  =  67.75   12  18   69.49( 262)    0   0  |    0   1  |   68.00  235 |   67.95  238 |   66.84  260
 243  Elon                    =  67.74   13  18   70.57( 211)    0   1  |    0   1  |   67.28  246 |   67.77  242 |   67.75  245
 244  Sacred Heart            =  67.73   14  17   68.54( 308)    0   1  |    0   1  |   67.55  242 |   66.94  254 |   68.46  237
 245  SE Missouri State(SEMO) =  67.66   11  17   69.56( 258)    0   1  |    0   1  |   68.17  233 |   68.14  236 |   66.09  275
 246  Drexel                  =  67.64   11  18   71.87( 171)    0   0  |    0   1  |   67.48  243 |   67.16  252 |   68.00  242
 247  NC Asheville            =  67.55   12  16   69.25( 275)    0   0  |    0   0  |   67.15  249 |   67.41  247 |   67.74  247
 248  Northern Colorado       =  67.53   13  15   68.13( 320)    0   0  |    0   0  |   67.65  239 |   67.29  249 |   67.33  250
 249  Fla. International      =  67.40   14  17   70.86( 197)    0   1  |    0   1  |   66.71  255 |   66.42  262 |   68.82  234
 250  Brown                   =  67.13   11  18   71.50( 181)    0   0  |    1   1  |   66.93  253 |   66.66  259 |   67.53  248
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 251  Wright State            =  67.08    9  20   72.56( 151)    0   1  |    0   1  |   66.10  268 |   67.47  246 |   67.15  255
 252  Tennessee Tech          =  67.08   10  18   70.19( 226)    0   0  |    0   0  |   67.30  245 |   67.55  244 |   65.81  280
 253  Portland State          =  67.02   13  14   69.22( 277)    0   0  |    0   1  |   66.53  258 |   66.28  269 |   67.98  243
 254  Ball State              =  66.97    6  23   74.36( 111)    0   1  |    0   2  |   67.14  251 |   68.35  233 |   64.33  300
 255  Central Florida(UCF)    =  66.97   11  18   72.55( 152)    0   0  |    0   5  |   66.36  260 |   66.08  272 |   68.20  240
 256  Siena                   =  66.87   11  20   70.57( 212)    0   0  |    0   0  |   67.17  248 |   66.63  260 |   66.47  267
 257  Delaware State          =  66.78   16  17   68.96( 288)    0   1  |    0   2  |   65.07  286 |   65.25  287 |   69.53  222
 258  Bradley                 =  66.70    8  24   73.48( 128)    0   5  |    0   5  |   67.15  250 |   67.30  248 |   64.98  287
 259  SIU-Edwardsville        =  66.69   10  16   69.22( 276)    0   0  |    0   0  |   66.83  254 |   66.67  258 |   66.21  273
 260  South Florida           =  66.64    8  23   74.85( 101)    0   0  |    0   4  |   66.19  263 |   66.74  255 |   66.57  266
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 261  Lamar                   =  66.63   11  15   69.62( 257)    0   1  |    0   5  |   66.19  265 |   65.69  280 |   67.77  244
 262  Saint Louis             =  66.55   10  21   73.95( 119)    0   1  |    0   6  |   66.03  269 |   66.10  271 |   67.21  252
 263  Northern Kentucky       =  66.54   11  17   69.67( 252)    0   2  |    0   2  |   65.68  276 |   67.04  253 |   66.31  270
 264  Weber State             =  66.50   11  17   69.73( 248)    0   1  |    0   3  |   66.57  257 |   66.38  264 |   66.21  272
 265  Hartford                =  66.41   13  16   68.97( 286)    0   1  |    0   1  |   66.30  262 |   65.57  282 |   67.13  256
 266  Hampton                 =  66.31   16  17   66.62( 341)    0   1  |    0   2  |   65.68  277 |   65.75  277 |   67.20  254
 267  Alabama State           =  66.31   17  10   61.64( 351)    0   2  |    0   2  |   65.49  279 |   66.29  268 |   66.73  263
 268  Grand Canyon            =  66.30   15  14   66.15( 345)    0   1  |    0   2  |   65.46  280 |   66.32  267 |   66.69  264
 269  Omaha(Neb.-Omaha)       =  66.28   11  17   68.92( 291)    0   0  |    0   0  |   65.86  274 |   66.74  256 |   65.72  281
 270  CS Bakersfield          =  66.27   11  19   67.46( 330)    0   0  |    0   1  |   66.58  256 |   67.26  251 |   64.07  303
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 271  Towson                  =  66.27   11  20   69.84( 240)    0   1  |    0   1  |   66.16  266 |   66.73  257 |   65.35  284
 272  Marshall                =  66.23    9  21   72.43( 155)    0   2  |    0   2  |   65.87  273 |   66.33  266 |   66.06  277
 273  Drake                   =  66.16    8  22   74.67( 103)    0   5  |    0   5  |   66.00  270 |   65.75  278 |   66.45  269
 274  Navy                    =  66.12   12  19   69.77( 245)    0   2  |    0   3  |   65.23  283 |   65.59  281 |   67.21  253
 275  Youngstown State        =  66.02    8  21   72.22( 162)    0   0  |    0   0  |   66.19  264 |   66.37  265 |   64.98  288
 276  Delaware                =  66.01   10  20   71.56( 179)    0   1  |    0   2  |   65.42  281 |   66.01  274 |   66.19  274
 277  Long Island U.(LIU)     =  65.98   12  18   69.15( 280)    0   0  |    0   1  |   65.93  271 |   65.13  289 |   66.67  265
 278  Seattle                 =  65.95   14  15   66.89( 338)    0   0  |    0   0  |   65.08  285 |   66.39  263 |   65.82  279
 279  Howard                  =  65.94   13  16   67.71( 327)    0   0  |    0   1  |   65.05  288 |   65.40  283 |   67.04  257
 280  Nevada                  =  65.93    7  22   73.81( 121)    0   0  |    0   3  |   65.88  272 |   66.20  270 |   65.25  286
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 281  CS Northridge           =  65.90    7  24   73.45( 131)    0   2  |    0   5  |   66.35  261 |   66.52  261 |   64.15  302
 282  Pennsylvania            =  65.85    9  19   71.91( 168)    0   1  |    0   1  |   65.11  284 |   65.32  284 |   66.80  261
 283  Kansas City(UMKC)       =  65.83   12  19   68.31( 315)    0   1  |    0   1  |   66.38  259 |   66.03  273 |   64.58  296
 284  Florida Atlantic        =  65.63    7  20   71.43( 183)    0   0  |    0   1  |   66.10  267 |   65.78  276 |   64.53  297
 285  College of Charleston   =  65.61    9  24   71.89( 169)    0   1  |    0   4  |   65.73  275 |   65.85  275 |   64.78  290
 286  IUPUI                   =  65.55   10  21   71.71( 175)    0   0  |    0   2  |   65.04  289 |   65.31  285 |   65.96  278
 287  Appalachian State       =  65.53   12  17   70.66( 204)    0   0  |    0   0  |   64.67  293 |   64.33  297 |   67.27  251
 288  Southern U.             =  65.35   15  17   66.64( 340)    0   2  |    0   2  |   64.55  296 |   64.89  290 |   66.25  271
 289  Illinois-Chicago        =  65.15    8  24   72.78( 146)    0   0  |    0   2  |   65.07  287 |   65.16  288 |   64.83  289
 290  Samford                 =  64.93   12  19   68.05( 321)    0   0  |    0   1  |   65.31  282 |   64.68  292 |   64.49  298
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 291  McNeese State           =  64.87   11  16   68.97( 287)    0   1  |    0   3  |   63.95  302 |   64.66  293 |   65.59  282
 292  Lipscomb                =  64.86   11  17   69.73( 249)    0   1  |    0   1  |   64.12  301 |   64.06  301 |   66.09  276
 293  Arkansas State          =  64.85   10  18   69.82( 242)    0   0  |    0   1  |   64.97  290 |   63.93  302 |   65.44  283
 294  CS Fullerton            =  64.81    7  22   72.68( 148)    0   0  |    0   1  |   64.48  297 |   64.86  291 |   64.68  294
 295  VMI                     =  64.71    9  19   69.80( 244)    0   1  |    0   2  |   64.86  291 |   64.59  294 |   64.34  299
 296  UMass Lowell            =  64.71   11  17   70.56( 213)    0   1  |    0   1  |   63.74  303 |   63.56  304 |   66.46  268
 297  NC Greensboro           =  64.70    8  22   69.25( 274)    0   1  |    0   2  |   64.61  295 |   65.70  279 |   62.93  308
 298  South Alabama           =  64.69   10  21   70.72( 202)    0   0  |    0   1  |   64.20  299 |   64.31  298 |   65.26  285
 299  Prairie View A&M        =  64.60   14  18   67.16( 336)    0   1  |    0   3  |   64.46  298 |   64.36  296 |   64.67  295
 300  Troy                    =  64.53    8  19   69.01( 285)    0   0  |    0   1  |   64.84  292 |   65.26  286 |   62.72  310
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 301  Furman                  =  64.39    9  22   70.09( 230)    0   1  |    0   1  |   65.64  278 |   63.43  306 |   63.81  304
 302  Loyola-Maryland         =  64.33   11  19   70.54( 214)    0   1  |    0   1  |   62.85  307 |   62.77  309 |   66.79  262
 303  Fairfield               =  64.19    7  24   70.61( 206)    0   1  |    0   1  |   64.67  294 |   64.41  295 |   62.94  307
 304  Southern Miss           =  63.69    7  20   73.01( 139)    0   0  |    0   1  |   63.53  304 |   62.61  313 |   64.68  293
 305  Wagner                  =  63.65    9  20   69.67( 253)    0   0  |    0   2  |   62.56  311 |   63.26  307 |   64.70  292
 306  New Orleans             =  63.60    8  18   68.45( 312)    0   0  |    0   2  |   64.18  300 |   63.49  305 |   62.72  309
 307  Niagara                 =  63.55    8  22   71.26( 185)    0   0  |    0   2  |   62.60  310 |   64.18  300 |   63.23  305
 308  Campbell                =  63.31    7  22   69.30( 271)    0   1  |    0   2  |   63.18  305 |   63.65  303 |   62.59  311
 309  Houston Baptist         =  63.25    8  16   69.97( 236)    0   0  |    0   2  |   61.88  315 |   62.61  314 |   64.76  291
 310  Southern Utah           =  62.94    9  19   68.64( 303)    0   0  |    0   1  |   62.83  308 |   62.66  311 |   63.02  306
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 311  SE Louisiana            =  62.92    8  23   68.20( 318)    0   2  |    0   4  |   62.36  312 |   64.19  299 |   61.13  320
 312  Jacksonville State      =  62.63   10  19   69.55( 259)    0   1  |    0   1  |   61.73  317 |   61.63  319 |   64.15  301
 313  Marist                  =  62.57    7  25   70.80( 200)    0   0  |    0   0  |   61.89  314 |   62.93  308 |   62.37  314
 314  Jackson State           =  62.17   11  21   65.81( 346)    0   0  |    0   1  |   62.17  313 |   62.74  310 |   60.92  323
 315  Fairleigh Dickinson     =  62.12    7  21   69.72( 250)    0   1  |    0   2  |   61.62  318 |   61.96  317 |   62.42  312
 316  North Dakota            =  62.07    6  22   69.98( 235)    0   2  |    0   2  |   62.64  309 |   62.46  315 |   60.41  326
 317  Idaho State             =  62.06    5  23   68.72( 299)    0   0  |    0   0  |   63.15  306 |   62.64  312 |   59.20  332
 318  Longwood                =  61.88    9  23   69.01( 284)    0   1  |    0   1  |   61.21  320 |   61.65  318 |   62.40  313
 319  Austin Peay             =  61.76    6  22   70.98( 194)    0   0  |    0   2  |   61.33  319 |   61.97  316 |   61.52  319
 320  The Citadel             =  61.67    8  19   68.91( 292)    0   1  |    0   1  |   61.87  316 |   60.99  320 |   61.90  318
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 321  Utah Valley             =  61.08    9  19   68.15( 319)    0   2  |    0   2  |   59.96  324 |   60.80  322 |   62.02  316
 322  Western Illinois        =  60.86    6  20   70.70( 203)    0   0  |    0   0  |   60.03  323 |   59.79  324 |   62.34  315
 323  Montana State           =  60.69    6  23   69.88( 239)    0   1  |    0   2  |   60.44  322 |   60.95  321 |   60.17  329
 324  Ark.-Pine Bluff         =  60.28   12  20   66.65( 339)    0   1  |    0   2  |   59.30  327 |   59.14  327 |   61.92  317
 325  Binghamton-NY           =  60.21    5  25   70.97( 195)    0   1  |    0   2  |   60.57  321 |   60.32  323 |   59.25  331
 326  Texas-Pan American      =  59.86    7  21   68.73( 298)    0   1  |    0   1  |   59.40  325 |   59.57  325 |   60.26  327
 327  Nicholls State          =  59.59    7  19   68.90( 294)    0   1  |    0   3  |   57.79  340 |   59.29  326 |   60.98  322
 328  Bethune-Cookman         =  59.22    9  21   64.64( 350)    0   0  |    0   0  |   59.34  326 |   59.06  328 |   58.92  335
 329  Coppin State            =  58.98    7  23   70.47( 217)    0   1  |    0   3  |   58.27  334 |   58.08  336 |   60.20  328
 330  SC State                =  58.96    9  22   67.87( 325)    0   1  |    0   1  |   57.95  338 |   57.82  338 |   60.57  325
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 331  Morgan State            =  58.90    7  24   68.91( 293)    0   1  |    0   1  |   58.82  329 |   58.95  329 |   58.53  338
 332  Kennesaw State          =  58.89    8  22   69.26( 273)    0   1  |    0   2  |   58.19  335 |   57.13  343 |   60.78  324
 333  Stetson                 =  58.86    6  22   68.63( 304)    0   0  |    0   1  |   58.64  332 |   58.72  332 |   58.88  337
 334  Presbyterian College    =  58.85    6  22   69.63( 254)    0   1  |    0   1  |   58.05  337 |   58.14  335 |   59.97  330
 335  Chicago State           =  58.80    5  24   71.07( 190)    0   1  |    0   1  |   58.34  333 |   58.77  331 |   58.89  336
 336  Abilene Christian       =  58.78    7  21   68.81( 296)    0   0  |    0   2  |   57.31  345 |   57.19  342 |   61.00  321
 337  Tennessee State         =  58.46    3  26   71.16( 187)    0   1  |    0   1  |   58.73  331 |   58.84  330 |   57.16  342
 338  NC A&T                  =  58.25    7  23   67.26( 335)    0   1  |    0   1  |   58.81  330 |   58.27  334 |   57.12  343
 339  Alabama A&M             =  58.24    8  20   65.74( 347)    0   0  |    0   1  |   58.84  328 |   57.79  339 |   57.75  340
 340  Jacksonville            =  58.24    7  22   68.01( 323)    0   0  |    0   2  |   57.32  344 |   57.78  340 |   59.18  333
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 341  Liberty                 =  58.03    4  24   68.38( 314)    0   0  |    0   0  |   57.67  342 |   58.59  333 |   57.17  341
 342  Savannah State          =  57.87    7  22   68.66( 302)    0   1  |    0   4  |   57.90  339 |   56.41  345 |   58.98  334
 343  Central Connecticut St. =  57.86    5  26   68.68( 300)    0   0  |    0   1  |   57.74  341 |   57.70  341 |   57.81  339
 344  UMBC                    =  57.64    4  26   69.18( 278)    0   1  |    0   1  |   58.15  336 |   57.92  337 |   56.12  344
 345  Maine                   =  56.77    3  27   71.60( 178)    0   1  |    0   1  |   57.34  343 |   56.90  344 |   55.44  345
 346  San Jose State          =  54.60    0  28   74.49( 106)    0   0  |    0   3  |   55.39  346 |   55.54  346 |   50.24  349
 347  Alcorn State            =  54.04    5  25   65.41( 348)    0   2  |    0   2  |   54.20  347 |   54.74  347 |   52.06  348
 348  Central Arkansas        =  52.95    2  27   68.62( 305)    0   0  |    0   1  |   53.26  348 |   52.80  348 |   52.36  347
 349  MVSU(Miss. Valley St.)  =  52.84    6  26   67.39( 332)    0   1  |    0   2  |   52.15  349 |   51.91  349 |   54.00  346
 350  Florida A&M             =  49.84    2  27   66.58( 342)    0   0  |    0   0  |   50.42  350 |   48.98  350 |   49.80  350
College Basketball 2014-2015    Div I games only  through games of 2015 March 16 Monday                                             
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | GOLDEN_MEAN  | PREDICTOR    | ELO_SCORE  
                HOME ADVANTAGE=[  3.35]                                               [  3.25]       [  3.32]       [  3.50]
 351  Grambling State         =  43.74    0  27   66.34( 343)    0   1  |    0   2  |   44.67  351 |   43.90  351 |   40.63  351
"""

elif config.date == 2013:

    #http://usatoday30.usatoday.com/sports/sagarin/bkt1213.htm
    lineparts = ["Rank","Team","Rating","W","L","Schedule","ScheduleRank","WinsVsTop25","LossesVsTop25","WinsVsTop50","LossesVsTop50","ELO_SCORE","ELO_RANK","PREDICTOR","PREDICTOR_RANK"]
    text = """                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
   1  Louisville              =  95.01   29   5   80.24(   8)    7   4  |   12   5  |   95.26    1 |   94.72    1
   2  Indiana                 =  92.48   27   6   79.68(  13)    7   3  |   11   6  |   91.65    3 |   93.51    3
   3  Florida                 =  92.29   26   7   78.97(  28)    3   3  |    5   5  |   91.17    5 |   93.86    2
   4  Kansas                  =  91.85   29   5   78.73(  34)    6   2  |   12   4  |   91.95    2 |   91.70    4
   5  Ohio State              =  91.42   26   7   79.87(  11)    6   6  |    9   7  |   91.56    4 |   91.24    6
   6  Gonzaga                 =  91.20   30   2   75.62( 103)    2   0  |    7   2  |   90.94    6 |   91.43    5
   7  Duke                    =  90.79   27   5   80.09(   9)    6   2  |   10   5  |   90.52    7 |   91.03    7
   8  Michigan State          =  89.80   24   8   81.36(   1)    5   6  |    9   8  |   89.95    9 |   89.61    9
   9  Georgetown              =  89.66   25   6   79.43(  20)    5   4  |    9   5  |   90.47    8 |   88.93   12
  10  Pittsburgh              =  89.08   24   8   76.86(  80)    2   6  |    6   7  |   88.78   12 |   89.34   10
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
  11  Michigan                =  89.04   25   7   79.91(  10)    5   6  |    9   6  |   89.03   10 |   89.01   11
  12  Wisconsin               =  88.80   23  11   81.24(   2)    5   7  |    9  10  |   88.05   15 |   89.65    8
  13  Syracuse                =  88.77   26   9   79.75(  12)    4   6  |    7   8  |   88.82   11 |   88.68   13
  14  Miami-Florida           =  88.32   27   6   79.46(  18)    7   2  |    9   2  |   88.71   13 |   87.91   14
  15  Saint Louis             =  87.74   27   6   75.73( 101)    1   1  |    6   1  |   88.34   14 |   87.17   16
  16  Missouri                =  87.26   23  10   77.75(  61)    1   2  |    5   6  |   86.91   21 |   87.58   15
  17  New Mexico              =  86.90   29   5   78.73(  35)    0   1  |    8   3  |   87.94   16 |   86.00   22
  18  Oklahoma State          =  86.80   24   8   78.50(  40)    3   4  |    7   7  |   86.94   20 |   86.61   18
  19  North Carolina          =  86.70   23  10   79.45(  19)    1   7  |    6   9  |   87.09   19 |   86.30   21
  20  Kansas State            =  86.61   26   7   78.59(  36)    3   6  |    8   7  |   87.74   17 |   85.64   26
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
  21  Creighton               =  86.59   27   7   75.92(  99)    1   0  |    3   2  |   86.27   25 |   86.87   17
  22  Marquette               =  86.56   23   8   79.61(  16)    6   4  |    7   7  |   87.30   18 |   85.87   23
  23  Arizona                 =  86.20   25   7   78.34(  43)    2   0  |    4   4  |   86.04   26 |   86.31   19
  24  Notre Dame              =  86.17   25   9   78.48(  41)    3   5  |    7   6  |   86.59   22 |   85.73   25
  25  NC State                =  86.14   24  10   78.52(  39)    2   6  |    5   8  |   86.52   24 |   85.73   24
  26  VCU(Va. Commonwealth)   =  85.67   26   8   76.47(  89)    0   4  |    3   5  |   85.06   27 |   86.30   20
  27  Memphis                 =  85.67   30   4   74.20( 122)    0   1  |    0   3  |   86.52   23 |   84.88   33
  28  Mississippi             =  85.03   26   8   75.95(  98)    3   2  |    3   3  |   85.00   28 |   85.01   31
  29  Iowa                    =  85.00   21  12   77.68(  63)    1   7  |    4   9  |   84.95   29 |   85.00   32
  30  Minnesota               =  84.98   20  12   80.81(   3)    3   6  |    7   9  |   84.57   34 |   85.37   27
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
  31  Baylor                  =  84.93   17  14   78.98(  26)    2   6  |    3  10  |   84.79   32 |   85.02   30
  32  San Diego State         =  84.74   20  10   78.15(  49)    1   4  |    3   7  |   84.66   33 |   84.77   34
  33  Iowa State              =  84.65   22  11   78.04(  52)    2   5  |    6   9  |   84.84   31 |   84.42   36
  34  Saint Mary's-Cal.       =  84.58   26   6   74.32( 120)    1   3  |    1   3  |   83.93   39 |   85.25   28
  35  Cincinnati              =  84.52   22  11   78.99(  25)    2   8  |    6   9  |   84.85   30 |   84.17   38
  36  Colorado State          =  84.21   23   8   77.44(  67)    0   2  |    2   5  |   84.02   38 |   84.37   37
  37  Kentucky                =  84.20   21  11   77.84(  57)    2   4  |    4   5  |   83.42   44 |   85.04   29
  38  Virginia                =  84.14   21  11   76.29(  94)    4   3  |    6   3  |   83.72   40 |   84.56   35
  39  UNLV                    =  84.12   24   9   77.34(  70)    1   3  |    6   5  |   84.23   35 |   83.97   39
  40  Villanova               =  83.61   19  13   80.25(   7)    4   5  |    5   6  |   84.10   37 |   83.11   43
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
  41  UCLA                    =  83.47   25   9   78.54(  37)    4   1  |    6   4  |   83.60   42 |   83.29   42
  42  Wichita State           =  83.37   26   8   75.56( 105)    1   2  |    3   2  |   82.98   47 |   83.74   40
  43  Oklahoma                =  83.33   20  11   79.11(  24)    2   5  |    5   7  |   83.67   41 |   82.96   45
  44  Illinois                =  83.18   21  12   80.54(   6)    3   8  |    6  10  |   83.02   46 |   83.30   41
  45  Butler                  =  83.02   25   8   78.53(  38)    4   3  |    4   5  |   84.13   36 |   82.02   54
  46  Connecticut             =  83.01   20  10   79.13(  23)    3   6  |    4   8  |   83.55   43 |   82.45   50
  47  Oregon                  =  82.91   26   8   76.32(  93)    1   0  |    5   2  |   83.16   45 |   82.63   48
  48  Stanford                =  82.70   18  14   78.31(  45)    0   3  |    1   8  |   82.62   49 |   82.74   47
  49  Maryland                =  82.62   22  12   76.47(  90)    3   5  |    3   8  |   82.70   48 |   82.49   49
  50  Belmont                 =  82.44   24   6   72.26( 163)    0   1  |    1   2  |   81.90   53 |   82.96   46
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
  51  Tennessee               =  82.38   20  12   78.73(  33)    2   2  |    4   7  |   82.50   50 |   82.22   53
  52  Colorado                =  82.38   21  11   78.91(  29)    1   3  |    7   4  |   82.34   51 |   82.37   51
  53  Middle Tennessee        =  81.94   28   5   70.96( 211)    0   1  |    1   2  |   80.99   59 |   82.98   44
  54  Alabama                 =  81.88   20  12   77.96(  54)    0   3  |    2   6  |   81.84   55 |   81.88   55
  55  Temple                  =  81.82   23   9   76.44(  91)    2   2  |    4   3  |   82.31   52 |   81.31   61
  56  California              =  81.69   20  11   78.20(  46)    1   2  |    4   6  |   81.79   56 |   81.55   58
  57  La Salle                =  81.60   21   9   76.15(  96)    0   2  |    3   3  |   81.55   57 |   81.59   57
  58  Boise State             =  81.50   19  10   77.68(  62)    1   3  |    4   7  |   81.84   54 |   81.12   63
  59  Purdue                  =  81.40   15  17   79.52(  17)    1   8  |    4  11  |   81.28   58 |   81.47   59
  60  Denver                  =  81.39   21   9   72.76( 150)    0   0  |    0   2  |   80.58   64 |   82.24   52
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
  61  Southern Miss           =  81.36   23   9   75.42( 106)    0   1  |    0   5  |   80.89   61 |   81.81   56
  62  Akron                   =  81.15   25   6   72.41( 158)    0   2  |    0   2  |   80.97   60 |   81.28   62
  63  Arkansas                =  80.82   19  13   77.24(  73)    2   5  |    4   6  |   80.68   62 |   80.92   64
  64  Davidson                =  80.70   25   7   69.94( 245)    0   3  |    0   3  |   79.99   70 |   81.42   60
  65  Valparaiso              =  80.37   25   7   71.77( 179)    0   2  |    0   2  |   80.23   66 |   80.47   67
  66  Providence              =  80.35   17  14   77.99(  53)    1   6  |    4   9  |   80.59   63 |   80.07   70
  67  Dayton                  =  80.31   17  14   76.05(  97)    0   1  |    0   4  |   80.22   68 |   80.36   69
  68  BYU                     =  80.08   20  11   74.49( 117)    0   3  |    0   7  |   79.60   74 |   80.54   66
  69  Saint Joseph's-Pa.      =  80.00   18  13   76.59(  86)    1   2  |    1   6  |   79.58   75 |   80.39   68
  70  Xavier-Ohio             =  79.89   17  14   77.54(  66)    1   0  |    3   3  |   80.05   69 |   79.68   72
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
  71  Northern Iowa           =  79.80   17  14   77.25(  72)    1   2  |    3   7  |   79.53   76 |   80.04   71
  72  Texas                   =  79.76   16  16   78.76(  32)    1   9  |    4  13  |   80.39   65 |   79.12   80
  73  Bucknell                =  79.74   27   5   71.09( 200)    0   1  |    0   1  |   80.22   67 |   79.23   76
  74  Illinois State          =  79.64   18  15   75.33( 107)    1   2  |    1   5  |   78.60   84 |   80.75   65
  75  Massachusetts           =  79.58   21  11   76.67(  84)    0   3  |    0   6  |   79.79   71 |   79.32   75
  76  Washington              =  79.44   18  15   78.08(  50)    1   3  |    2  10  |   79.68   72 |   79.16   78
  77  Vanderbilt              =  79.42   16  17   77.90(  55)    0   2  |    1   9  |   79.33   77 |   79.47   74
  78  Georgia                 =  79.14   15  17   77.80(  60)    0   4  |    1   6  |   79.62   73 |   78.63   85
  79  New Mexico State        =  79.12   23  10   73.19( 139)    0   2  |    0   2  |   79.26   79 |   78.93   81
  80  Detroit                 =  79.09   18  12   74.35( 119)    0   3  |    0   4  |   78.64   82 |   79.52   73
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
  81  Arizona State           =  78.98   21  12   75.60( 104)    0   3  |    2   7  |   79.26   78 |   78.66   84
  82  Stony Brook-NY          =  78.91   23   7   69.45( 272)    0   0  |    0   2  |   78.61   83 |   79.18   77
  83  Ohio                    =  78.75   24   9   71.70( 183)    0   0  |    0   3  |   78.35   86 |   79.12   79
  84  LSU                     =  78.63   19  12   76.64(  85)    1   4  |    1   6  |   78.98   80 |   78.24   86
  85  Richmond                =  78.45   18  14   75.67( 102)    0   2  |    1   5  |   77.96   90 |   78.91   82
  86  Texas A&M               =  78.24   18  15   77.13(  77)    1   3  |    3   6  |   78.27   87 |   78.16   87
  87  Florida State           =  78.00   18  15   78.98(  27)    1   8  |    4  10  |   78.67   81 |   77.30   98
  88  St. John's              =  77.98   16  15   78.37(  42)    1   7  |    3  10  |   78.44   85 |   77.50   97
  89  Evansville              =  77.97   17  14   75.06( 109)    0   3  |    2   5  |   77.89   91 |   78.00   88
  90  Stephen F. Austin       =  77.96   23   4   67.89( 319)    0   0  |    1   0  |   78.12   88 |   77.74   91
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
  91  Boston College          =  77.87   16  17   78.19(  47)    0   8  |    2  11  |   78.11   89 |   77.58   95
  92  Rutgers                 =  77.86   15  16   78.86(  31)    1   7  |    1  12  |   77.82   92 |   77.86   90
  93  South Dakota State      =  77.74   22   9   70.30( 230)    1   0  |    1   2  |   77.76   93 |   77.68   92
  94  Washington State        =  77.67   13  19   76.57(  87)    0   4  |    1   8  |   77.32   99 |   77.98   89
  95  Georgia Tech            =  77.66   16  15   77.05(  78)    1   6  |    4   8  |   77.69   94 |   77.57   96
  96  North Dakota State      =  77.55   22   9   70.15( 236)    0   1  |    0   2  |   76.45  112 |   78.69   83
  97  Louisiana Tech          =  77.52   25   6   71.04( 205)    0   0  |    0   0  |   77.36   98 |   77.63   94
  98  Iona                    =  77.50   20  13   73.27( 138)    0   0  |    0   0  |   77.66   95 |   77.28   99
  99  UTEP                    =  77.42   18  14   74.81( 112)    0   1  |    1   5  |   77.55   97 |   77.24  100
 100  Princeton               =  77.41   16  11   72.30( 162)    0   1  |    0   1  |   77.13  101 |   77.64   93
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 101  Southern California     =  77.10   14  18   79.64(  15)    1   3  |    4   8  |   77.19  100 |   76.97  103
 102  Oregon State            =  77.08   14  18   76.72(  82)    0   2  |    0   7  |   76.97  104 |   77.14  101
 103  Air Force               =  77.03   15  13   77.83(  58)    1   2  |    3   8  |   77.55   96 |   76.47  111
 104  Clemson                 =  76.99   13  18   77.35(  69)    0   8  |    1  10  |   76.89  106 |   77.04  102
 105  Harvard                 =  76.98   18   9   72.50( 153)    0   0  |    0   3  |   76.95  105 |   76.96  104
 106  West Virginia           =  76.93   13  19   78.87(  30)    0   8  |    0  15  |   77.04  103 |   76.77  107
 107  Santa Clara             =  76.92   19  11   72.77( 149)    1   3  |    1   5  |   76.88  107 |   76.91  105
 108  Weber State             =  76.81   24   6   67.13( 331)    0   0  |    0   0  |   76.78  109 |   76.79  106
 109  Fresno State            =  76.71    9  19   79.31(  22)    0   2  |    2   8  |   76.86  108 |   76.53  109
 110  Wyoming                 =  76.60   17  13   77.26(  71)    0   3  |    1   8  |   77.07  102 |   76.10  116
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 111  Utah State              =  76.45   20  10   71.48( 188)    0   0  |    0   1  |   76.13  116 |   76.73  108
 112  Mercer                  =  76.34   21  11   69.50( 269)    0   1  |    0   1  |   76.22  114 |   76.41  112
 113  Kent State              =  76.31   19  13   72.53( 152)    0   0  |    0   0  |   76.20  115 |   76.37  113
 114  Seton Hall              =  76.20   15  18   78.16(  48)    0   9  |    1  11  |   75.86  120 |   76.50  110
 115  South Florida           =  76.19   12  19   79.36(  21)    1   8  |    2  12  |   76.63  111 |   75.71  119
 116  Nebraska                =  76.17   15  18   80.67(   4)    0  10  |    2  15  |   76.75  110 |   75.56  123
 117  St. Bonaventure         =  75.97   14  15   75.74( 100)    0   2  |    0   5  |   75.92  119 |   75.97  117
 118  George Washington       =  75.91   13  17   76.69(  83)    0   3  |    0   5  |   75.52  126 |   76.26  115
 119  Central Florida(UCF)    =  75.87   18  11   73.47( 133)    0   2  |    1   4  |   75.94  118 |   75.75  118
 120  Lehigh                  =  75.83   20   9   70.01( 243)    0   1  |    0   3  |   75.29  131 |   76.33  114
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 121  Indiana State           =  75.74   17  14   77.23(  74)    2   3  |    4   6  |   75.75  123 |   75.68  121
 122  Loyola-Maryland         =  75.73   21  11   71.72( 181)    0   0  |    0   1  |   75.85  121 |   75.57  122
 123  Utah                    =  75.62   13  18   77.80(  59)    0   2  |    1   7  |   76.09  117 |   75.11  127
 124  Wake Forest             =  75.60   13  18   78.07(  51)    2   4  |    3   8  |   75.81  122 |   75.35  125
 125  Green Bay               =  75.59   17  15   72.80( 148)    1   1  |    1   2  |   75.58  124 |   75.56  124
 126  Florida Gulf Coast      =  75.53   22  10   70.06( 240)    1   1  |    1   3  |   75.33  130 |   75.69  120
 127  Charlotte               =  75.47   21  11   74.99( 110)    0   3  |    1   4  |   76.35  113 |   74.58  135
 128  Northwestern            =  75.36   13  19   79.64(  14)    0   7  |    3  15  |   75.48  127 |   75.20  126
 129  Murray State            =  75.22   19  10   71.07( 203)    0   0  |    1   1  |   75.40  128 |   75.00  128
 130  Pacific                 =  75.15   20  12   73.32( 137)    0   1  |    1   2  |   75.39  129 |   74.86  133
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 131  Drake                   =  75.07   14  17   76.28(  95)    1   2  |    1   6  |   75.11  133 |   74.98  129
 132  Penn State              =  75.05   10  21   80.63(   5)    1   9  |    1  13  |   75.12  132 |   74.93  130
 133  Montana                 =  74.93   23   6   68.33( 307)    0   0  |    0   1  |   75.56  125 |   74.25  137
 134  Eastern Kentucky        =  74.74   22   9   69.81( 252)    0   0  |    0   3  |   74.55  135 |   74.89  131
 135  George Mason            =  74.73   18  14   72.94( 144)    0   1  |    1   2  |   74.60  134 |   74.80  134
 136  Wright State            =  74.61   20  12   71.98( 173)    0   0  |    0   1  |   74.28  139 |   74.89  132
 137  Manhattan               =  74.31   14  18   73.52( 131)    0   1  |    0   1  |   74.27  140 |   74.31  136
 138  Northwestern State      =  74.23   19   8   69.74( 257)    0   0  |    0   1  |   74.39  137 |   74.01  144
 139  East Carolina           =  74.21   14  12   74.12( 123)    0   1  |    0   3  |   74.37  138 |   73.99  146
 140  Long Beach State        =  74.20   17  13   74.29( 121)    0   4  |    0   5  |   74.23  141 |   74.13  140
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 141  Niagara                 =  74.18   19  13   72.25( 164)    0   1  |    0   1  |   74.17  142 |   74.14  139
 142  Texas-Arlington         =  74.15   19  13   72.45( 156)    0   1  |    0   2  |   74.16  143 |   74.09  143
 143  Canisius                =  74.03   18  13   72.95( 143)    0   1  |    0   2  |   74.00  146 |   74.01  145
 144  Vermont                 =  74.00   21  11   68.95( 290)    0   0  |    0   1  |   73.99  147 |   73.96  147
 145  Virginia Tech           =  73.99   13  19   78.33(  44)    1   7  |    2  12  |   74.46  136 |   73.48  156
 146  Robert Morris           =  73.97   23  10   68.07( 313)    0   0  |    0   0  |   73.69  150 |   74.22  138
 147  San Francisco           =  73.95   13  16   74.65( 114)    0   2  |    0   7  |   74.07  145 |   73.79  151
 148  UC Irvine               =  73.94   18  15   73.06( 141)    0   0  |    0   2  |   74.10  144 |   73.73  152
 149  Cal Poly-SLO            =  73.93   16  13   72.42( 157)    0   0  |    1   1  |   73.73  149 |   74.09  142
 150  UAB                     =  73.84   15  17   74.59( 116)    0   2  |    0   4  |   73.74  148 |   73.89  148
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 151  Drexel                  =  73.77   13  18   72.91( 145)    0   0  |    0   1  |   73.62  151 |   73.86  149
 152  Tulane                  =  73.61   18  14   70.95( 212)    0   0  |    0   2  |   73.08  159 |   74.10  141
 153  College of Charleston   =  73.56   24   9   69.33( 275)    0   1  |    1   1  |   73.57  153 |   73.50  155
 154  Western Michigan        =  73.44   19  12   71.47( 190)    0   2  |    0   2  |   73.33  154 |   73.50  154
 155  Delaware                =  73.25   19  14   72.72( 151)    0   3  |    1   4  |   73.59  152 |   72.87  162
 156  Nevada                  =  73.21   11  19   77.61(  65)    0   2  |    0   9  |   73.30  155 |   73.08  157
 157  Arkansas State          =  73.21   18  12   69.10( 282)    0   0  |    0   0  |   72.56  166 |   73.82  150
 158  Rider                   =  73.09   18  14   72.36( 161)    0   0  |    0   0  |   73.22  156 |   72.92  161
 159  Houston                 =  73.07   18  12   69.16( 279)    0   0  |    0   1  |   72.49  168 |   73.61  153
 160  Boston U.               =  73.00   17  12   69.86( 251)    0   0  |    0   1  |   73.18  157 |   72.77  163
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 161  Oral Roberts            =  72.91   17  14   70.53( 225)    0   1  |    0   4  |   72.82  162 |   72.95  160
 162  Tennessee State         =  72.80   16  14   72.24( 165)    0   1  |    1   4  |   73.10  158 |   72.44  167
 163  Long Island U.          =  72.79   20  13   68.26( 310)    0   0  |    0   2  |   73.02  160 |   72.50  166
 164  Tulsa                   =  72.78   16  15   73.65( 129)    0   1  |    0   4  |   72.92  161 |   72.60  165
 165  DePaul                  =  72.77   11  21   77.65(  64)    0   8  |    0  13  |   72.55  167 |   72.95  159
 166  Fairfield               =  72.73   19  15   72.19( 167)    0   0  |    0   1  |   72.42  169 |   72.98  158
 167  Albany-NY               =  72.71   24  10   68.33( 306)    0   1  |    0   1  |   72.63  164 |   72.75  164
 168  San Diego               =  72.49   14  18   74.38( 118)    0   2  |    0   6  |   72.73  163 |   72.20  173
 169  James Madison           =  72.46   20  14   70.57( 224)    0   0  |    0   1  |   72.58  165 |   72.29  171
 170  Lafayette               =  72.29   18  15   70.64( 223)    0   0  |    0   4  |   72.09  173 |   72.44  168
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 171  Northeastern            =  72.27   20  12   71.37( 192)    0   0  |    1   0  |   72.35  170 |   72.13  178
 172  Buffalo                 =  72.25   12  20   73.41( 134)    0   0  |    0   0  |   72.14  172 |   72.31  170
 173  Loyola-Chicago          =  72.11   14  16   71.47( 189)    0   1  |    0   1  |   71.94  175 |   72.24  172
 174  Toledo                  =  72.11   15  13   70.65( 222)    0   0  |    0   1  |   72.17  171 |   72.01  179
 175  Georgia State           =  72.07   14  16   71.11( 198)    0   1  |    0   1  |   71.75  180 |   72.35  169
 176  Auburn                  =  72.05    9  23   77.14(  76)    0   2  |    0   7  |   71.92  177 |   72.14  177
 177  Western Illinois        =  71.94   20   8   68.61( 297)    0   0  |    0   0  |   71.98  174 |   71.86  180
 178  SMU                     =  71.90   14  17   72.09( 170)    0   0  |    0   1  |   71.58  182 |   72.18  175
 179  Towson                  =  71.77   17  13   71.88( 174)    0   1  |    0   1  |   71.72  181 |   71.78  181
 180  Army                    =  71.76   15  15   69.53( 267)    0   0  |    0   0  |   71.30  185 |   72.17  176
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 181  Wagner                  =  71.67   19  12   68.89( 291)    0   1  |    0   1  |   71.92  176 |   71.38  184
 182  Western Kentucky        =  71.48   19  15   70.70( 220)    0   1  |    0   3  |   71.43  184 |   71.48  183
 183  South Carolina          =  71.46   14  18   74.70( 113)    0   3  |    1   4  |   71.76  178 |   71.11  186
 184  Rhode Island            =  71.34    8  21   76.93(  79)    1   1  |    1   4  |   71.52  183 |   71.11  185
 185  Marshall                =  71.29   12  19   74.02( 125)    0   0  |    0   5  |   71.76  179 |   70.77  190
 186  Charleston Southern     =  71.27   16  12   67.83( 324)    0   1  |    0   2  |   70.94  195 |   71.55  182
 187  Bradley                 =  71.06   16  16   73.82( 127)    0   3  |    0   5  |   71.24  188 |   70.84  188
 188  Texas Southern          =  71.02   17  14   66.58( 336)    0   2  |    0   3  |   69.78  210 |   72.18  174
 189  Youngstown State        =  70.85   14  15   72.98( 142)    0   0  |    0   0  |   71.24  187 |   70.41  202
 190  South Alabama           =  70.81   16  12   70.27( 232)    0   0  |    0   0  |   71.01  193 |   70.55  199
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 191  USC Upstate             =  70.80   14  17   69.74( 255)    0   2  |    0   3  |   70.50  201 |   71.05  187
 192  Southern Illinois       =  70.79   13  17   74.97( 111)    0   3  |    1   4  |   71.16  190 |   70.37  203
 193  Illinois-Chicago        =  70.79   16  15   72.88( 146)    0   1  |    1   1  |   71.09  191 |   70.43  201
 194  Oakland-Mich.           =  70.70   14  16   73.13( 140)    0   2  |    0   2  |   70.69  197 |   70.67  194
 195  Loyola Marymount        =  70.68   10  22   74.61( 115)    0   4  |    0   7  |   70.98  194 |   70.32  204
 196  Fla. International      =  70.67   18  14   71.06( 204)    0   1  |    0   1  |   70.63  198 |   70.65  195
 197  Columbia                =  70.65   10  16   70.73( 219)    0   0  |    1   0  |   70.47  202 |   70.79  189
 198  Yale                    =  70.64   12  17   72.87( 147)    0   1  |    0   3  |   70.51  200 |   70.72  192
 199  Idaho                   =  70.52   11  18   73.65( 130)    0   1  |    0   1  |   70.28  203 |   70.71  193
 200  Missouri State          =  70.47    9  22   76.47(  88)    0   3  |    0   7  |   70.93  196 |   69.95  209
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 201  Elon                    =  70.44   19  11   68.54( 301)    0   1  |    0   2  |   70.21  205 |   70.62  196
 202  Quinnipiac              =  70.44   15  16   69.52( 268)    0   0  |    0   1  |   70.60  199 |   70.24  205
 203  Gardner-Webb            =  70.41   18  12   67.83( 323)    0   1  |    0   3  |   70.28  204 |   70.49  200
 204  Texas Tech              =  70.40   11  20   77.22(  75)    0   8  |    1  13  |   71.29  186 |   69.44  215
 205  Hawai'i                 =  70.38   16  14   70.14( 237)    0   1  |    0   4  |   70.09  206 |   70.62  197
 206  NC Central              =  70.35   19   9   67.02( 332)    0   1  |    0   2  |   69.90  209 |   70.75  191
 207  Mount St. Mary's        =  70.32   18  14   69.79( 254)    0   3  |    0   3  |   71.09  192 |   69.49  214
 208  CS Fullerton            =  70.16   12  18   71.14( 196)    0   0  |    0   1  |   70.08  207 |   70.19  207
 209  UC Santa Barbara        =  70.05    9  20   73.71( 128)    0   0  |    0   1  |   70.06  208 |   69.99  208
 210  Mississippi State       =  69.99   10  22   77.39(  68)    0   5  |    1   7  |   71.21  189 |   68.67  225
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 211  SE Missouri State(SEMO) =  69.86   15  16   67.97( 317)    0   2  |    0   3  |   69.74  212 |   69.94  211
 212  Bryant                  =  69.83   19  11   68.44( 305)    0   1  |    0   1  |   69.75  211 |   69.86  212
 213  Bowling Green           =  69.71   11  19   71.84( 176)    0   1  |    0   1  |   69.14  220 |   70.23  206
 214  Southern U.             =  69.69   20   9   63.70( 347)    0   0  |    0   1  |   68.72  227 |   70.57  198
 215  Morgan State            =  69.62   17  15   67.58( 325)    0   0  |    0   1  |   69.24  218 |   69.94  210
 216  William & Mary          =  69.51   12  17   70.99( 209)    0   0  |    0   0  |   69.29  216 |   69.68  213
 217  Norfolk State           =  69.27   21  11   67.26( 330)    0   1  |    0   2  |   69.66  213 |   68.83  222
 218  Savannah State          =  69.12   17  14   68.59( 299)    0   4  |    0   4  |   69.13  221 |   69.07  218
 219  UC Davis                =  69.08   14  17   71.00( 207)    0   1  |    0   2  |   69.16  219 |   68.95  219
 220  Stetson                 =  69.02   14  16   69.67( 261)    0   1  |    0   2  |   69.25  217 |   68.74  223
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 221  NC Asheville            =  68.99   13  16   69.87( 250)    0   2  |    0   2  |   68.62  229 |   69.30  217
 222  Ark.-Little Rock        =  68.89   16  15   70.45( 227)    0   0  |    0   2  |   69.30  214 |   68.42  229
 223  Eastern Michigan        =  68.89   13  18   71.45( 191)    0   2  |    0   3  |   69.30  215 |   68.42  228
 224  Jacksonville State      =  68.86   15  11   69.92( 247)    0   0  |    0   4  |   68.79  225 |   68.89  220
 225  Morehead State          =  68.79   13  18   72.45( 155)    0   0  |    0   4  |   69.02  222 |   68.52  227
 226  High Point              =  68.75   15  13   67.00( 333)    0   0  |    0   0  |   68.04  240 |   69.38  216
 227  CS Northridge           =  68.67   12  17   71.71( 182)    0   0  |    0   1  |   68.62  230 |   68.68  224
 228  Florida Atlantic        =  68.56   13  18   70.48( 226)    0   2  |    0   2  |   68.81  224 |   68.26  234
 229  TCU                     =  68.50   10  21   76.76(  81)    1   5  |    2  10  |   68.73  226 |   68.22  236
 230  Fort Wayne(IPFW)        =  68.27   14  17   69.09( 283)    0   1  |    0   1  |   68.09  239 |   68.41  230
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 231  Seattle                 =  68.26    7  22   71.68( 185)    0   0  |    0   2  |   67.60  248 |   68.84  221
 232  Pepperdine              =  68.20   11  18   73.39( 135)    0   2  |    0   4  |   68.37  232 |   67.99  240
 233  Marist                  =  68.18   10  21   72.37( 159)    0   0  |    0   0  |   68.22  235 |   68.09  238
 234  Northern Colorado       =  68.15   11  18   68.67( 295)    0   0  |    0   2  |   68.46  231 |   67.79  244
 235  Brown                   =  68.14   12  15   70.73( 218)    0   1  |    0   1  |   68.32  233 |   67.92  243
 236  Sam Houston State       =  68.13   14  17   68.86( 292)    0   1  |    0   1  |   67.97  241 |   68.25  235
 237  Cleveland State         =  68.11   11  18   74.09( 124)    0   2  |    0   2  |   68.92  223 |   67.19  258
 238  Louisiana-Lafayette     =  68.10   12  20   71.08( 201)    0   1  |    0   1  |   67.80  244 |   68.35  231
 239  Fordham                 =  68.10    7  24   77.87(  56)    0   2  |    0   6  |   68.69  228 |   67.43  253
 240  Duquesne                =  68.08    8  22   76.39(  92)    0   3  |    0   5  |   68.12  237 |   67.99  239
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 241  St. Francis-NY          =  68.04   12  18   70.25( 233)    0   0  |    0   1  |   67.83  243 |   68.20  237
 242  NC A&T                  =  67.99   18  16   67.29( 328)    0   0  |    0   2  |   67.67  247 |   68.26  232
 243  Ball State              =  67.91   14  15   70.38( 228)    0   1  |    0   2  |   68.12  238 |   67.66  248
 244  Coastal Carolina        =  67.91   11  15   68.76( 293)    0   0  |    0   1  |   67.21  253 |   68.53  226
 245  North Florida(UNF)      =  67.89   12  19   71.23( 194)    0   2  |    0   5  |   68.15  236 |   67.59  251
 246  Appalachian State       =  67.84   13  16   68.52( 303)    0   1  |    0   1  |   67.92  242 |   67.72  246
 247  Hartford                =  67.83   17  13   69.04( 288)    0   0  |    0   0  |   68.28  234 |   67.33  256
 248  Texas-San Antonio(UTSA) =  67.83   10  22   72.37( 160)    0   0  |    0   1  |   67.68  246 |   67.94  242
 249  CS Bakersfield          =  67.74   10  16   71.69( 184)    0   0  |    0   3  |   67.74  245 |   67.70  247
 250  Western Carolina        =  67.66   12  19   69.61( 264)    0   1  |    0   3  |   66.99  257 |   68.26  233
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 251  Miami-Ohio              =  67.58    8  22   73.97( 126)    0   2  |    0   2  |   67.51  249 |   67.60  250
 252  North Texas             =  67.57   11  19   70.02( 242)    0   2  |    0   3  |   67.15  254 |   67.94  241
 253  Old Dominion            =  67.48    5  25   71.60( 187)    0   0  |    1   1  |   67.14  255 |   67.76  245
 254  Holy Cross              =  67.41   12  18   70.94( 214)    0   0  |    0   0  |   67.39  251 |   67.38  255
 255  Wofford                 =  67.39   12  19   69.98( 244)    0   0  |    0   1  |   67.33  252 |   67.41  254
 256  Pennsylvania            =  67.33    9  22   72.48( 154)    0   0  |    0   2  |   67.06  256 |   67.55  252
 257  Texas State             =  67.31   11  22   72.15( 169)    0   0  |    0   0  |   66.92  258 |   67.65  249
 258  North Dakota            =  67.15   14  16   68.10( 312)    0   1  |    0   1  |   67.46  250 |   66.78  261
 259  Central Michigan        =  66.87   10  20   72.16( 168)    0   1  |    0   2  |   66.36  265 |   67.31  257
 260  Liberty                 =  66.73   12  20   68.31( 308)    0   1  |    0   1  |   66.33  266 |   67.07  259
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 261  Cornell                 =  66.72   12  18   71.08( 202)    0   2  |    0   2  |   66.52  260 |   66.87  260
 262  South Dakota            =  66.47    8  20   71.23( 195)    0   2  |    0   3  |   66.41  263 |   66.49  262
 263  Tennessee Tech          =  66.43   10  17   71.03( 206)    0   1  |    0   3  |   66.89  259 |   65.90  267
 264  Portland                =  66.38    9  21   75.16( 108)    0   3  |    0   8  |   66.51  261 |   66.21  263
 265  Georgia Southern        =  66.17   12  19   69.58( 266)    0   0  |    0   1  |   66.47  262 |   65.82  269
 266  Northern Kentucky       =  66.16   11  16   69.48( 270)    0   1  |    0   1  |   66.06  267 |   66.21  264
 267  Maine                   =  66.13   10  19   70.20( 235)    0   0  |    0   0  |   66.36  264 |   65.84  268
 268  Eastern Illinois        =  65.77   11  20   69.13( 280)    0   1  |    0   2  |   65.80  272 |   65.70  270
 269  American U.             =  65.76   10  20   70.76( 217)    0   2  |    0   3  |   65.48  276 |   65.98  266
 270  Troy                    =  65.70   12  21   69.35( 274)    0   0  |    0   0  |   65.92  268 |   65.43  273
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 271  SE Louisiana            =  65.64   11  18   70.22( 234)    0   3  |    0   3  |   65.87  270 |   65.36  274
 272  Central Connecticut St. =  65.56   13  17   69.46( 271)    0   2  |    0   2  |   65.85  271 |   65.21  276
 273  Milwaukee               =  65.44    6  24   73.47( 132)    0   1  |    0   1  |   65.75  273 |   65.08  277
 274  NC Greensboro           =  65.42    7  22   68.76( 294)    0   1  |    0   1  |   64.63  289 |   66.11  265
 275  Bethune-Cookman         =  65.38   12  20   68.20( 311)    0   1  |    0   1  |   65.28  278 |   65.44  272
 276  Jacksonville            =  65.32   12  18   69.67( 262)    0   2  |    0   2  |   65.53  275 |   65.06  279
 277  Winthrop                =  65.26   11  17   69.08( 285)    0   1  |    0   2  |   64.93  282 |   65.54  271
 278  Delaware State          =  65.20   13  18   68.28( 309)    0   1  |    0   2  |   65.63  274 |   64.71  285
 279  Lipscomb                =  65.08   11  18   70.95( 213)    0   0  |    0   5  |   65.88  269 |   64.15  294
 280  Sacred Heart            =  65.08    9  20   70.86( 216)    0   0  |    0   0  |   65.10  281 |   65.01  281
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 281  NJIT(New Jersey Tech)   =  65.07   12  13   64.91( 345)    0   0  |    0   1  |   64.81  286 |   65.27  275
 282  Hofstra                 =  65.00    6  25   72.08( 171)    0   0  |    0   0  |   65.29  277 |   64.66  286
 283  Samford                 =  65.00   10  21   69.10( 281)    0   2  |    0   4  |   64.88  283 |   65.07  278
 284  Dartmouth               =  64.96    8  19   70.97( 210)    0   0  |    0   0  |   64.82  285 |   65.04  280
 285  Siena                   =  64.88    8  24   72.04( 172)    0   0  |    0   0  |   65.25  279 |   64.45  288
 286  Hampton                 =  64.85   14  17   66.55( 337)    0   0  |    0   0  |   64.74  287 |   64.91  283
 287  New Hampshire           =  64.84    8  20   70.11( 239)    0   0  |    0   1  |   64.71  288 |   64.92  282
 288  NC Wilmington           =  64.83    9  20   71.80( 178)    0   0  |    0   0  |   65.21  280 |   64.38  289
 289  VMI                     =  64.72   11  17   67.84( 321)    0   0  |    0   0  |   64.86  284 |   64.53  287
 290  Colgate                 =  64.62   11  21   71.10( 199)    0   2  |    0   3  |   64.34  292 |   64.84  284
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 291  Ark.-Pine Bluff         =  64.23   16  14   66.17( 340)    0   1  |    0   3  |   64.36  291 |   64.06  296
 292  McNeese State           =  64.20   11  17   69.66( 263)    0   1  |    0   2  |   64.42  290 |   63.93  298
 293  Sacramento State        =  64.17   12  15   67.28( 329)    0   0  |    0   0  |   64.17  294 |   64.11  295
 294  Campbell                =  64.16   11  19   67.85( 320)    0   1  |    0   3  |   63.90  295 |   64.37  291
 295  Saint Peter's           =  64.11    9  21   71.26( 193)    0   0  |    0   0  |   63.78  298 |   64.38  290
 296  Eastern Washington      =  64.07   10  21   67.97( 318)    0   0  |    0   1  |   63.86  297 |   64.22  292
 297  Austin Peay             =  64.00    6  23   69.91( 248)    0   0  |    0   2  |   63.89  296 |   64.05  297
 298  Nicholls State          =  63.87    9  21   69.60( 265)    0   2  |    0   2  |   63.51  299 |   64.16  293
 299  Chattanooga             =  63.59   11  19   68.63( 296)    0   1  |    0   1  |   63.41  300 |   63.73  300
 300  Utah Valley             =  63.54   10  18   67.34( 327)    0   0  |    0   0  |   63.27  302 |   63.75  299
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 301  East Tennessee State    =  63.42    9  22   71.87( 175)    0   2  |    0   4  |   64.28  293 |   62.41  311
 302  Rice                    =  63.40    4  25   73.36( 136)    0   0  |    0   1  |   63.22  305 |   63.52  301
 303  Portland State          =  63.00    6  20   68.01( 315)    0   1  |    0   2  |   62.68  309 |   63.27  302
 304  Montana State           =  62.98   11  17   66.87( 334)    0   0  |    0   0  |   62.91  306 |   63.01  305
 305  UC Riverside            =  62.97    4  24   71.82( 177)    0   0  |    0   0  |   63.39  301 |   62.48  309
 306  San Jose State          =  62.96    8  20   72.21( 166)    0   1  |    0   1  |   63.25  304 |   62.61  307
 307  SIU-Edwardsville        =  62.90    7  18   69.32( 276)    0   2  |    0   3  |   62.74  308 |   63.01  304
 308  Radford                 =  62.90   10  19   67.84( 322)    0   0  |    0   0  |   62.50  311 |   63.24  303
 309  Central Arkansas        =  62.87   11  17   67.97( 316)    0   1  |    0   1  |   62.89  307 |   62.81  306
 310  Northern Arizona        =  62.54   11  21   69.74( 256)    0   1  |    0   3  |   63.26  303 |   61.68  317
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 311  Southern Utah           =  62.49    9  20   68.59( 300)    0   1  |    0   1  |   62.53  310 |   62.40  312
 312  Chicago State           =  62.36    7  21   69.07( 287)    0   2  |    0   3  |   62.21  315 |   62.46  310
 313  Monmouth-NJ             =  62.14   10  21   70.05( 241)    0   2  |    0   4  |   62.22  314 |   62.02  313
 314  Kansas City(UMKC)       =  62.09    7  24   71.00( 208)    0   3  |    0   4  |   62.41  312 |   61.69  316
 315  Texas A&M-CorpusChristi =  62.04    5  23   70.67( 221)    0   0  |    0   2  |   61.49  319 |   62.50  308
 316  Northern Illinois       =  61.77    4  25   71.72( 180)    0   0  |    0   0  |   61.93  317 |   61.56  318
 317  Texas-Pan American      =  61.68   12  16   66.24( 339)    0   0  |    0   1  |   61.83  318 |   61.48  319
 318  UMBC                    =  61.66    7  23   70.36( 229)    0   1  |    0   1  |   61.95  316 |   61.30  320
 319  Omaha(Neb.-Omaha)       =  61.56   10  19   70.27( 231)    0   1  |    0   2  |   62.28  313 |   60.70  323
 320  Coppin State            =  61.53    7  24   70.14( 238)    0   1  |    0   2  |   61.26  320 |   61.75  315
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 321  Jackson State           =  61.44   11  18   65.53( 342)    0   0  |    0   2  |   60.94  322 |   61.85  314
 322  Navy                    =  61.16    7  23   69.70( 260)    0   0  |    0   0  |   61.13  321 |   61.14  321
 323  Idaho State             =  60.59    5  24   69.07( 286)    0   0  |    0   1  |   60.17  327 |   60.94  322
 324  Louisiana-Monroe        =  60.39    4  23   71.66( 186)    0   0  |    0   1  |   60.64  323 |   60.08  325
 325  Houston Baptist         =  60.35   11  17   66.37( 338)    0   0  |    0   1  |   60.62  324 |   60.03  326
 326  Prairie View A&M        =  60.35   12  19   64.67( 346)    0   0  |    0   1  |   60.52  325 |   60.12  324
 327  The Citadel             =  59.98    6  22   68.98( 289)    0   0  |    0   0  |   60.37  326 |   59.51  329
 328  Florida A&M             =  59.70    6  23   69.30( 277)    0   0  |    0   0  |   59.44  330 |   59.91  327
 329  IUPUI                   =  59.60    4  26   71.12( 197)    0   1  |    0   3  |   59.68  328 |   59.47  330
 330  Howard                  =  59.32    6  23   68.46( 304)    0   1  |    0   3  |   59.28  332 |   59.31  331
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 331  Saint Francis-Pa.       =  59.30    5  24   69.93( 246)    0   1  |    0   1  |   59.27  333 |   59.29  332
 332  Tennessee-Martin        =  58.99    7  21   69.80( 253)    0   1  |    0   4  |   59.43  331 |   58.46  335
 333  Longwood                =  58.95    6  25   68.54( 302)    0   2  |    0   3  |   59.48  329 |   58.32  336
 334  Kennesaw State          =  58.84    3  27   69.73( 258)    0   2  |    0   2  |   57.87  337 |   59.61  328
 335  Presbyterian College    =  58.77    5  24   69.09( 284)    0   2  |    0   2  |   58.50  335 |   58.99  334
 336  Furman                  =  58.66    5  24   69.45( 273)    0   0  |    0   0  |   59.00  334 |   58.25  337
 337  Alcorn State            =  58.21    9  23   67.54( 326)    0   2  |    0   3  |   56.95  339 |   59.16  333
 338  Alabama State           =  57.82    9  22   65.41( 344)    0   1  |    0   1  |   57.54  338 |   58.03  338
 339  Fairleigh Dickinson     =  57.59    7  24   69.70( 259)    0   0  |    0   1  |   58.26  336 |   56.75  341
 340  Alabama A&M             =  57.42    9  20   65.51( 343)    0   0  |    0   1  |   56.70  341 |   58.00  339
College Basketball 2012-2013          Div I games only   through 2013 March 17 Sunday
                                RATING    W   L  SCHEDL(RANK) VS top 25 | VS top 50 | ELO_SCORE    | PREDICTOR  
                HOME ADVANTAGE=[  3.34]                                               [  3.33]       [  3.39]
 341  SC State                =  57.01    4  24   68.60( 298)    0   1  |    0   3  |   56.82  340 |   57.15  340
 342  MVSU(Miss. Valley St.)  =  56.30    5  23   66.58( 335)    0   0  |    0   3  |   55.92  343 |   56.60  342
 343  Md.-Eastern Shore(UMES) =  55.95    2  26   69.24( 278)    0   0  |    0   3  |   55.89  344 |   55.96  344
 344  Lamar                   =  55.95    3  28   70.86( 215)    0   1  |    0   3  |   55.75  345 |   56.09  343
 345  New Orleans             =  55.93    4  18   68.06( 314)    0   0  |    0   1  |   56.27  342 |   55.52  345
 346  Binghamton-NY           =  55.47    2  27   69.87( 249)    0   1  |    0   1  |   55.38  346 |   55.51  346
 347  Grambling State         =  43.97    0  28   66.06( 341)    0   0  |    0   0  |   43.54  347 |   44.30  347
"""


def sanitize_teamname(name):
    result = name.replace('State','St.').replace('NC ','North Carolina ').replace('Saint','St.')
    result = result.replace('Albany-NY','Albany')
    #result = result.replace('VCU(Va. Commonwealth)','Virginia Commonwealth')
    result = result.replace('VCU(Va. Commonwealth)','VCU')
    result = result.replace('Southern U.','Southern')
    result = result.replace('UNLV','Nevada Las Vegas')
    result = result.replace('Miami-Florida','Miami FL')
    result = result.replace("St. Mary's-Cal.","St. Mary's")
    result = result.replace('Xavier-Ohio','Xavier')
    return result
#print sanitize_teamname("Saint MAry's-Cal.")

sagarindata = {}
for line in text.split('\n'):
    if not line.strip():
        continue
    parts = line.strip().split()
    if not parts:
        continue
    if parts[0] in ["RATING","HOME","College"]:
        continue
    left,right = line.split('=')
    rank = left.split()[0]
    team = ' '.join(left.split()[1:])
    rank = int(rank)
    team = sanitize_teamname(team)
    if team not in sagarindata:
        sagarindata[team] = {}
    sagarindata[team]['Rank'] = rank
    sagarindata[team]['Rating'] = float(right.split()[0])


