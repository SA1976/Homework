"""Дан текст состоящий из нескольких строки. Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите последнее.
Задачу необходимо решить с использованием словаря.
"""


def string_cleaning(str_for_cln):
    list_for_cleaning = list('.[],{}|—±§!@$%^&*()<>-_+:;?\"\'\\')

    for strng in list_for_cleaning:  # чистим строки от знаков препинания
        for a in range(len(str_for_cln)):
            str_in_process = str_for_cln[a].replace(strng, ' ', str_for_cln[a].count(strng))
            str_for_cln[a] = str_in_process.strip()

    for a in range(len(str_for_cln)):  # чистим строки от двойных пробелов
        if str_for_cln[a].count('  ') != 0:
            while str_for_cln[a].count('  ') != 0:
                str_in_process = str_for_cln[a].replace('  ', ' ', str_for_cln[a].count('  '))
                str_for_cln[a] = str_in_process.strip()

    return str_for_cln


# текст из Википедии, руками удалены абзацы
initial_string = '" В 1582 году на григорианский календарь перешли Испания, Португалия (как провинция Испании), Италия," \
                  " Речь Посполитая (Великое княжество Литовское и Польша), Франция, Лотарингия[источник не указан 1019 " \
                  "дней].К концу 1583 года к ним присоединились Голландия, Бельгия, Брабант, Фландрия, Льеж, Аугсбург, " \
                  "Трир, Бавария, Зальцбург, Регенсбург, часть Австрии и Тироль. Не обошлось без курьёзов. Например, в " \
                  "Бельгии и Голландии 1 января 1583 года наступило сразу после 21 декабря 1582 года и всё население " \
                  "осталось в том году без Рождества[13]. В 1583 году Григорий XIII направил Константинопольскому " \
                  "патриарху Иеремии II посольство с предложением перейти на новый календарь. В конце 1583 года на соборе" \
                  " в Константинополе предложение было отвергнуто как не соответствующее каноническим правилам празднования" \
                  " Пасхи, а последователям нового календаря провозглашена анафема[21].В 1584 году завершила свой переход" \
                  " на григорианский календарь Австрия, начала переход Швейцария (кантоны Люцерн, Ури, Швиц, Цуг, Фрайбург," \
                  " Золотурн), Силезия, Вестфалия и Испанские колонии в Америке. В XVI веке перешла на григорианский календарь" \
                  " католическая часть Швейцарии, протестантские кантоны перешли в 1753 году, а последний, Гризон, — в 1811" \
                  " году[источник не указан 3368 дней]. В ряде случаев переход на григорианский календарь сопровождался серьёзными" \
                  " беспорядками. Например, когда польский король Стефан Баторий ввёл в Риге новый календарь в 1584 году," \
                  " местные купцы подняли мятеж, заявив, что сдвиг на 10 дней срывает их сроки поставок и приводит к значительным убыткам." \
                  " Мятежники разгромили рижскую церковь и убили несколько муниципальных служащих. Справиться с «календарными " \
                  "беспорядками» удалось только летом 1589 года[22].В некоторых странах, перешедших на григорианский календарь," \
                  " впоследствии возобновлялось юлианское летосчисление в результате их присоединения к другим государствам." \
                  " В связи с разновременным переходом стран на григорианский календарь могут возникать фактические ошибки" \
                  " восприятия: например, иногда говорится, что Инка Гарсиласо де ла Вега, Мигель де Сервантес и Уильям " \
                  "Шекспир умерли в один день — 23 апреля 1616 года[23]. На самом деле Шекспир умер на 10 дней позже, " \
                  "чем Инка Гарсиласо (в католической Испании новый стиль действовал с самого введения его папой, а " \
                  "Великобритания перешла на новый календарь только в 1752 году), и на 11 дней позже чем Сервантес " \
                  "(который умер 22 апреля, но был похоронен 23 апреля).В перешедшей по решению короля Георга II на " \
                  "григорианский календарь 2 сентября 1752 года Британии пришлось сдвигать дату вперёд уже не на 10, а " \
                  "на 11 дней, поскольку с момента вступления в силу нового календаря в континентальной Европе миновал " \
                  "уже целый век, и накопился ещё один лишний день[13]. После 2-го сразу наступило 14 сентября.Подданные" \
                  " остались недовольны решением, сделавшим их старше. В стране были замечены протесты под лозунгом: " \
                  "«Верните нам наши одиннадцать дней!», который присутствует в частности на одной из гравюр серии «Выборы»," \
                  " созданной Уильямом Хогартом. Временами вспыхивали бунты, иногда приводившие к гибели людей, например," \
                  " в Бристоле[13].Введение нового календаря имело также и серьёзные финансовые последствия для сборщиков" \
                  " налогов и податей. В 1753 году — первом полном году по григорианскому календарю — банкиры отказались" \
                  " платить налоги, дожидаясь положенных 11 дней после привычной даты окончания сборов — 25 марта. В " \
                  "результате финансовый год в Великобритании начался лишь 6 апреля. Эта дата сохранилась и до сегодняшних" \
                  " дней как символ больших перемен, произошедших 250 лет назад[13].В Швеции решили отменять високосные " \
                  "дни с 1700 по 1740 годы.В 1700 году был отменён первый високосный день. Потом началась война, и про перевод забыли." \
                  " Таким образом, страна жила по своему собственному шведскому календарю. В 1711 году Карл XII признал это непрактичным, решил вернуться к старому стилю и добавить " \
                  "в феврале 2 дня.Поэтому в Швеции было 30 февраля 1712 года.Лишь в 1753 году был введён новый стиль.При " \
                  "этом после 17 февраля последовало сразу 1 марта[источник не указан 3368 дней].Необычным был переход на " \
                  "григорианский календарь на Аляске, так как там он сочетался с переносом линии перемены даты. Поэтому " \
                  "после пятницы 6 октября 1867 года по старому стилю следовала ещё одна пятница 18 октября 1867 года" \
                  " по новому стилю.В 1872 году решение о переходе с традиционного лунно-солнечного на григорианский " \
                  "календарь приняла Япония, так что следующим днём после «второго дня двенадцатого месяца пятого года " \
                  "Мэйдзи» стало 1 января 1873 года, в результате чего календарь Японии был приведён в соответствие с " \
                  "календарём основных западных держав (за исключением России). Тем не менее, в официальных документах " \
                  "одновременно продолжает использоваться система нэнго. Например, год 1868 может быть записан как " \
                  "первый год Мэйдзи, 1912 — Тайсё 1, 1926 — Сёва 1, 1989 — Хэйсэй 1, и так далее.В обычной практике, " \
                  "однако, применяется летосчисление от рождества Христова по «западному календарю» (西暦, seireki)," \
                  " ставший в течение XX века в Японии основным.Корея приняла григорианский календарь 1 января 1896 " \
                  "года[источник не указан 2094 дня] при активном участии Ю Кил-чуна[24]. Хотя согласно принятому " \
                  "календарю установилась нумерация месяцев, но ещё в продолжении 1895—1897 годов продолжилась " \
                  "старая нумерация лет по первому году правления династии Чосон, по которой 1896 год " \
                  "григорианского календаря соответствовал 1392 году Чосон[25].Между 1897 и 1910 годами и вновь с 1948" \
                  " до 1962 год использовалось корейское начало календарной эры. Между 1910 и 1945 годами, когда Корея " \
                  "была под японским управлением, применялось японское летосчисление. С 1945 до 1961 годы в Южной Корее" \
                  " григорианский календарь был совмещён с летосчислением от основания государства Кочосон в 2333 году " \
                  "до н. э. (считается годом ранее[что?]), легендарным началом правления Дан-Гуна. Таким образом, эти " \
                  "годы по счислению Данги (단기) нумеровались с 4278 по 4294. Эта нумерация неофициально использовалась " \
                  "и до этого вместе с корейским лунным календарём, иногда используется и в настоящее время.[прояснить] " \
                  "В Северной Корее с 8 июля 1997 года принято новое «летосчисление чучхе», началом которого является " \
                  "1912 год — год рождения Ким Ир Сена.Китайская Республика официально приняла григорианский календарь " \
                  "при своём провозглашении с 1 января 1912 года, но континентальный Китай вступил в период военной " \
                  "диктатуры с властью различных полевых командиров, использовавших различные календари. С объединением" \
                  " Китая под властью Гоминьдана в октябре 1928 года Национальное правительство постановило, что с 1 " \
                  "января 1929 года будет использоваться григорианский календарь. Тем не менее, Китай сохранил китайскую" \
                  " традицию нумерации месяцев, а началом летосчисления был назначен первый год провозглашения Китайской" \
                  " Республики — 1912 год. Эта система всё ещё используется на Тайване, считающем себя преемником " \
                  "Китайской Республики. После провозглашения в 1949 году Китайской Народной Республики континентальный " \
                  "Китай продолжил использовать григорианский календарь, но были отменены нумерация и летосчисление, " \
                  "введённые прежним правительством, и установлено соответствие с летосчислением от рождества Христова, " \
                  "принятым в СССР и на Западе.В России на территории, находившейся под контролем советской власти, " \
                  "григорианский календарь был введён декретом Совнаркома от 26 января 1918 года, согласно которому в 1918" \
                  " году после 31 января следовало 14 февраля. На территориях бывшей Российской империи, " \
                  "находившихся под контролем других государственных образований, возникших после падения Временного " \
                  "правительства, даты официального введения нового стиля отличаются. Так, Временное Сибирское правительство" \
                  " ввело новый стиль декретом от 31 августа 1918 года, постановив считать день 1 октября 1918 днём 14 " \
                  "октября 1918 года[26].А на Юге России продолжали жить по старому стилю вплоть до перехода территории" \
                  " под власть большевиков.Таким образом, в ряде стран, в том числе и в России, в 1900 году был день 29 " \
                  "февраля, тогда как в большинстве стран его не было.Одними из последних на григорианский календарь " \
                  "перешли Греция в 1923 году[18], Турция в 1926 году и Египет в 1928 году[13]. Другие арабские страны " \
                  "в гражданской жизни также перешли на григорианский календарь, последней стала Саудовская Аравия " \
                  "(2016)[27].До сих пор не перешли на григорианский календарь Эфиопия (в стране используется эфиопский календарь)" \
                  "[13], Иран и Афганистан (иранский календарь), Непал (непальский календарь).В следующих странах параллельно" \
                  " используются григорианский и национальный календари: Израиль (еврейский календарь), Индия (Единый " \
                  "национальный календарь Индии), Бангладеш (бенгальский календарь).В Таиланде принят тайский солнечный" \
                  " календарь, который представляет собой григорианский календарь, но с другим летосчислением.Летосчисление" \
                  " нашей эры и национальное летосчисление параллельно используются в Китайской Республике (Тайвань) " \
                  "(календарь Миньго), КНДР (календарь чучхе), Японии (летосчисление по девизам правления).С 1923 года " \
                  "большинство поместных православных церквей, за исключением Русской, Иерусалимской, Грузинской, " \
                  "Сербской и Афона, приняло похожий на григорианский новоюлианский календарь, совпадающий с ним до 2800" \
                  " года.Он также был формально введён патриархом Тихоном для употребления в Русской православной церкви " \
                  "15 октября 1923 года. Однако это нововведение хотя и было принято практически всеми московскими приходами," \
                  " но в общем вызвало несогласие в Церкви, поэтому уже 8 ноября патриарх Тихон распорядился «повсеместное и " \
                  "обязательное введение нового стиля в церковное употребление временно отложить». Таким образом, новый стиль " \
                  "действовал в РПЦ только 24 дня.В 1948 году на Московском совещании Православных церквей постановлено, что Пасха, " \
                  "так же, как и все переходящие праздники, должна рассчитываться по александрийской пасхалии (юлианскому календарю), " \
                  "а непереходящие — по тому календарю, по которому живёт Поместная церковь.Финляндская православная церковь празднует " \
                  "Пасху по григорианскому календарю."'


list_of_str = string_cleaning(initial_string.split('.'))  # создаем список строк, убирая знаки препинания

lst_lst_word = [str.split(' ') for str in list_of_str]  # создаем список списков слов для этого, делим строки на слова

word_dict = {}

for row in lst_lst_word:
    for element in row:
        word_dict[element] = word_dict.get(element, 0) + 1
# word_dict.get(element, 0) - достает из словаря значение ключа element, если такого ключа еще
# нет то, get вернет 0 и затем добавится 1. если элемент есть,
# то вернет текущее значение и к нему добавится 1

for key in word_dict.keys(): #поиск максимального значения в словаре и его ключа
    if word_dict[key] == max(word_dict.values()):
        max_key = key

print()

print('Max rate: \'', max_key, '\':', word_dict[max_key], 'times')