# Generated by Django 3.1.2 on 2020-11-01 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2b_api', '0014_application_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='breed',
            field=models.CharField(choices=[('абиссинская', 'абиссинская'), ('американская жесткошерстная', 'американская жесткошерстная'), ('американская короткошерстная', 'американская короткошерстная'), ('американский бобтейл', 'американский бобтейл'), ('американский кёрл', 'американский кёрл'), ('ангорская', 'ангорская'), ('балинезийская', 'балинезийская'), ('бенгальская', 'бенгальская'), ('беспородная', 'беспородная'), ('бирма', 'бирма'), ('бирманская пятнисто-краповая', 'бирманская пятнисто-краповая'), ('бомбейская', 'бомбейская'), ('британская голубая', 'британская голубая'), ('британская короткошерстная', 'британская короткошерстная'), ('бурма', 'бурма'), ('бурмилла', 'бурмилла'), ('гаванна', 'гаванна'), ('герман рекс', 'герман рекс'), ('девон рекс', 'девон рекс'), ('домашняя', 'домашняя'), ('донский сфинкс', 'донский сфинкс'), ('другая', 'другая'), ('европейская короткошерстная', 'европейская короткошерстная'), ('египетская мау', 'египетская мау'), ('канадский сфинкс', 'канадский сфинкс'), ('кимрик', 'кимрик'), ('корат', 'корат'), ('корниш-рекс', 'корниш-рекс'), ('курильский бобтейл', 'курильский бобтейл'), ('манкс', 'манкс'), ('манчкин', 'манчкин'), ('мейн кун', 'мейн кун'), ('меконгский бобтейл', 'меконгский бобтейл'), ('мексиканская', 'мексиканская'), ('метис', 'метис'), ('мингонский бобтейл', 'мингонский бобтейл'), ('мэйн кун', 'мэйн кун'), ('невская маскарадная', 'невская маскарадная'), ('норвежская лесная дымчато-голубая', 'норвежская лесная дымчато-голубая'), ('ориенталская короткошерстная', 'ориенталская короткошерстная'), ('ориентальская длинношерстная', 'ориентальская длинношерстная'), ('охос азулес', 'охос азулес'), ('оцикет', 'оцикет'), ('персидская', 'персидская'), ('пиксибоб', 'пиксибоб'), ('русская голубая', 'русская голубая'), ('рысь домашняя', 'рысь домашняя'), ('рэгдол', 'рэгдол'), ('селкирк-рекс', 'селкирк-рекс'), ('сиамская', 'сиамская'), ('сибирская', 'сибирская'), ('сингапура', 'сингапура'), ('скоттиш страйт', 'скоттиш страйт'), ('скоттиш фолд', 'скоттиш фолд'), ('сноу-шу', 'сноу-шу'), ('сомали', 'сомали'), ('сфинкс', 'сфинкс'), ('тайская', 'тайская'), ('тифани', 'тифани'), ('тонкинез', 'тонкинез'), ('турецкий ван', 'турецкий ван'), ('цейлонская', 'цейлонская'), ('шартрез', 'шартрез'), ('шиншилла', 'шиншилла'), ('шотландская вислоухая', 'шотландская вислоухая'), ('экзотическая короткошерстная', 'экзотическая короткошерстная'), ('японский бобтейл', 'японский бобтейл'), ('австралийская борзая, кенгуровая', 'австралийская борзая, кенгуровая'), ('австралийская овчарка', 'австралийская овчарка'), ('австралийский терьер', 'австралийский терьер'), ('азавак', 'азавак'), ('аиди, атласская овчарка', 'аиди, атласская овчарка'), ('айну', 'айну'), ('акбаш', 'акбаш'), ('Акита - ину', 'Акита - ину'), ('акита ину', 'акита ину'), ('акита-ину', 'акита-ину'), ('алабай', 'алабай'), ('алапахский чистокровный бульдог', 'алапахский чистокровный бульдог'), ('альпийский спаниель', 'альпийский спаниель'), ('альпине даксбракке', 'альпине даксбракке'), ('аляскинский маламут', 'аляскинский маламут'), ('американский бульдог', 'американский бульдог'), ('американский водяной спаниель', 'американский водяной спаниель'), ('американский кокер спаниель', 'американский кокер спаниель'), ('американский питбультерьер', 'американский питбультерьер'), ('американский стафордшир-терьер', 'американский стафордшир-терьер'), ('американский той-фокстерьер', 'американский той-фокстерьер'), ('американский фоксхаунд', 'американский фоксхаунд'), ('американский эскимоский шпиц', 'американский эскимоский шпиц'), ('анатолийский карабаш', 'анатолийский карабаш'), ('английская овчарка', 'английская овчарка'), ('английский бульдог', 'английский бульдог'), ('английский водяной спаниель', 'английский водяной спаниель'), ('английский кокер спаниель', 'английский кокер спаниель'), ('английский мастиф', 'английский мастиф'), ('английский пойнтер', 'английский пойнтер'), ('английский сеттер', 'английский сеттер'), ('английский спрингер-спаниель', 'английский спрингер-спаниель'), ('английский той-терьер', 'английский той-терьер'), ('английский фоксхаунд', 'английский фоксхаунд'), ('аппенцеллер', 'аппенцеллер'), ('аргентинский дог', 'аргентинский дог'), ('арденский бувье', 'арденский бувье'), ('армант, египетская овчарка', 'армант, египетская овчарка'), ('артезиано-нормандский бассет', 'артезиано-нормандский бассет'), ('артуазская гончая', 'артуазская гончая'), ('арьежская гончая', 'арьежская гончая'), ('афганская борзая', 'афганская борзая'), ('афганская гончая', 'афганская гончая'), ('аффенпинчер', 'аффенпинчер'), ('баварская горная гончая', 'баварская горная гончая'), ('балканская гончая', 'балканская гончая'), ('банджарская борзая', 'банджарская борзая'), ('барбе', 'барбе'), ('бардино махеро', 'бардино махеро'), ('басенджи', 'басенджи'), ('баскетмейкер', 'баскетмейкер'), ('бассетхаунд', 'бассетхаунд'), ('беардед колли (хайланд колли)', 'беардед колли (хайланд колли)'), ('бедлингтон терьер', 'бедлингтон терьер'), ('белый английский терьер', 'белый английский терьер'), ('бельгийская лакенуа', 'бельгийская лакенуа'), ('бельгийская малинуа', 'бельгийская малинуа'), ('бельгийский брак', 'бельгийский брак'), ('бельгийский гриффон', 'бельгийский гриффон'), ('бельгийский грюнендаль', 'бельгийский грюнендаль'), ('бельгийский ловенар', 'бельгийский ловенар'), ('бельгийский тервюрен', 'бельгийский тервюрен'), ('бергамаско, бергамская овчарка', 'бергамаско, бергамская овчарка'), ('бернер лауфхунд', 'бернер лауфхунд'), ('бернская горная пастушья собака', 'бернская горная пастушья собака'), ('бернский зенненхунд', 'бернский зенненхунд'), ('беспородная', 'беспородная'), ('бигль', 'бигль'), ('бийи', 'бийи'), ('бишон фризе', 'бишон фризе'), ('бладхаунд', 'бладхаунд'), ('блю лейси', 'блю лейси'), ('бобтейл, староанглийская овчарка', 'бобтейл, староанглийская овчарка'), ('бойкин спаниель', 'бойкин спаниель'), ('боксёр', 'боксёр'), ('Болонка', 'Болонка'), ('болонский бишон', 'болонский бишон'), ('большая англо-французская гончая', 'большая англо-французская гончая'), ('большая голубая гасконская гончая', 'большая голубая гасконская гончая'), ('большая древесная гончая', 'большая древесная гончая'), ('большая пиринейская собака', 'большая пиринейская собака'), ('большая швейцарская горная пасту', 'большая швейцарская горная пасту'), ('большой вандейский гриффон', 'большой вандейский гриффон'), ('большой мюнстерлендер', 'большой мюнстерлендер'), ('большой немецкий шпиц', 'большой немецкий шпиц'), ('большой французский брак', 'большой французский брак'), ('бордер колли', 'бордер колли'), ('бордер терьер', 'бордер терьер'), ('бордосский дог (французский мастифф)', 'бордосский дог (французский мастифф)'), ('борзой, русская псовая борзая', 'борзой, русская псовая борзая'), ('бородатая колли', 'бородатая колли'), ('босерон', 'босерон'), ('боснийская грубошерстная гончая', 'боснийская грубошерстная гончая'), ('бостон-терьер', 'бостон-терьер'), ('брабансон', 'брабансон'), ('брак дюпюи', 'брак дюпюи'), ('брандл-брак', 'брандл-брак'), ('бретонский эпаньоль', 'бретонский эпаньоль'), ('бриар', 'бриар'), ('бруно-де-юра', 'бруно-де-юра'), ('брюссельский гриффон', 'брюссельский гриффон'), ('булленбайзер', 'булленбайзер'), ('бульдог англии старого типа', 'бульдог англии старого типа'), ('бульмастиф', 'бульмастиф'), ('бультерьер', 'бультерьер'), ('бультерьер миниатюрный', 'бультерьер миниатюрный'), ('бурбонский брак', 'бурбонский брак'), ('бурбуль', 'бурбуль'), ('веймаренер', 'веймаренер'), ('Вельш корги', 'Вельш корги'), ('вельш корги кардиган', 'вельш корги кардиган'), ('вельш корги пемброук', 'вельш корги пемброук'), ('вельш-спрингер-спаниель', 'вельш-спрингер-спаниель'), ('вельш-терьер', 'вельш-терьер'), ('венгерская борзая', 'венгерская борзая'), ('вест хайленд уайт терьер', 'вест хайленд уайт терьер'), ('вестфальский таксообразный брак', 'вестфальский таксообразный брак'), ('ветерхаунд, голландский спаниель', 'ветерхаунд, голландский спаниель'), ('водяной спаниель', 'водяной спаниель'), ('водяной твид спаниель', 'водяной твид спаниель'), ('вольпино итальано', 'вольпино итальано'), ('восточно-европейская овчарка', 'восточно-европейская овчарка'), ('восточносибирская лайка', 'восточносибирская лайка'), ('выжла, венгерская легавая', 'выжла, венгерская легавая'), ('гавайская собака пои', 'гавайская собака пои'), ('гаванский бишон', 'гаванский бишон'), ('гамильтонстёваре', 'гамильтонстёваре'), ('ганноверская гончая', 'ганноверская гончая'), ('германский дратхаар', 'германский дратхаар'), ('германский жесткошерстный пойнте', 'германский жесткошерстный пойнте'), ('германский короткошерстный пойнт', 'германский короткошерстный пойнт'), ('герта пойнтер', 'герта пойнтер'), ('гладкошерстный ретривер', 'гладкошерстный ретривер'), ('гладкошерстный фокстерьер', 'гладкошерстный фокстерьер'), ('глен-оф-имаал-терьер', 'глен-оф-имаал-терьер'), ('голая собака инков', 'голая собака инков'), ('голландская овчарка', 'голландская овчарка'), ('голландский смаусхонд', 'голландский смаусхонд'), ('голландский тульпхонд', 'голландский тульпхонд'), ('голубой гасконский бассет', 'голубой гасконский бассет'), ('голубой овернский брак', 'голубой овернский брак'), ('голубой пикардийский эпаньоль', 'голубой пикардийский эпаньоль'), ('голубой хиллер', 'голубой хиллер'), ('голштинская гончая', 'голштинская гончая'), ('гончая плотта', 'гончая плотта'), ('гончая стефена', 'гончая стефена'), ('гончая тальбота', 'гончая тальбота'), ('гордон-сеттер', 'гордон-сеттер'), ('гранди поденгу португезу', 'гранди поденгу португезу'), ('грейхаунд', 'грейхаунд'), ('гренландская собака', 'гренландская собака'), ('греческая заячья гончая', 'греческая заячья гончая'), ('греческая овчарка', 'греческая овчарка'), ('Гриффон', 'Гриффон'), ('гриффон кортальса', 'гриффон кортальса'), ('далматин', 'далматин'), ('датский брохольмер', 'датский брохольмер'), ('денди-динмонт терьер', 'денди-динмонт терьер'), ('джек рассел терьер', 'джек рассел терьер'), ('джек-рассел-терьер', 'джек-рассел-терьер'), ('джиндо', 'джиндо'), ('Доберман', 'Доберман'), ('доберман-пинчер', 'доберман-пинчер'), ('дратхаар', 'дратхаар'), ('древер', 'древер'), ('древесная тенессийская тигровая', 'древесная тенессийская тигровая'), ('дрентская куропаточная собака', 'дрентская куропаточная собака'), ('другая', 'другая'), ('дункер', 'дункер'), ('западно-сибирская лайка', 'западно-сибирская лайка'), ('зауерландский брак', 'зауерландский брак'), ('зауерландский хольцбрак', 'зауерландский хольцбрак'), ('золотистый ретривер', 'золотистый ретривер'), ('ирландский водяной спаниель', 'ирландский водяной спаниель'), ('ирландский волкодав (вольфхаунд)', 'ирландский волкодав (вольфхаунд)'), ('ирландский красно-белый сеттер', 'ирландский красно-белый сеттер'), ('ирландский сеттер', 'ирландский сеттер'), ('ирландский терьер', 'ирландский терьер'), ('исландская собака', 'исландская собака'), ('испанский брак, испанская легавая', 'испанский брак, испанская легавая'), ('испанский гальго, испанская борзая', 'испанский гальго, испанская борзая'), ('испанский мастиф', 'испанский мастиф'), ('истрийская гончая', 'истрийская гончая'), ('итальянский брак', 'итальянский брак'), ('йемтхунд, шведский элкхаунд', 'йемтхунд, шведский элкхаунд'), ('йоркширский терьер', 'йоркширский терьер'), ('ка де бо', 'ка де бо'), ('Кавалер кинг чарльз спаниель', 'Кавалер кинг чарльз спаниель'), ('кавказская овчарка', 'кавказская овчарка'), ('кай кен', 'кай кен'), ('кай лео', 'кай лео'), ('кан да серра ди айреш', 'кан да серра ди айреш'), ('кан да серра ди эштрела', 'кан да серра ди эштрела'), ('кан ди агуа', 'кан ди агуа'), ('кангал', 'кангал'), ('кане корсо', 'кане корсо'), ('каракачанская овчарка', 'каракачанская овчарка'), ('карело-финская лайка', 'карело-финская лайка'), ('карельская медвежья собака', 'карельская медвежья собака'), ('карликовый пинчер', 'карликовый пинчер'), ('каролинская собака', 'каролинская собака'), ('карстская (красская) овчарка', 'карстская (красская) овчарка'), ('каталонская овчарка', 'каталонская овчарка'), ('кеесхонд', 'кеесхонд'), ('келпи', 'келпи'), ('кентукская шел хип', 'кентукская шел хип'), ('керн-терьер', 'керн-терьер'), ('керри блю терьер', 'керри блю терьер'), ('керри-бигль', 'керри-бигль'), ('кисю', 'кисю'), ('китайская хохлатая собака', 'китайская хохлатая собака'), ('кламбер спаниель', 'кламбер спаниель'), ('коикерхондье', 'коикерхондье'), ('колли, шотландская овчарка', 'колли, шотландская овчарка'), ('комондор, венгерская овчарка', 'комондор, венгерская овчарка'), ('котон де тулеар', 'котон де тулеар'), ('крапчато-голубой кунхаунд', 'крапчато-голубой кунхаунд'), ('красный кунхаунд', 'красный кунхаунд'), ('кромфорлендер', 'кромфорлендер'), ('ксолойтцкуинтли', 'ксолойтцкуинтли'), ('кувас', 'кувас'), ('кунхаунд уолкера', 'кунхаунд уолкера'), ('курляндская гончая', 'курляндская гончая'), ('курцхаар', 'курцхаар'), ('курчавый ретривер', 'курчавый ретривер'), ('куунхаунд', 'куунхаунд'), ('лабрадор', 'лабрадор'), ('лабрадор ретривер', 'лабрадор ретривер'), ('лабрадор-ретривер', 'лабрадор-ретривер'), ('лаготто-романьоло', 'лаготто-романьоло'), ('лангедокская пастушья собака', 'лангедокская пастушья собака'), ('лангхаар', 'лангхаар'), ('ландсир', 'ландсир'), ('ланкаширский хилер', 'ланкаширский хилер'), ('лапинкойра, финнский лаппхунд', 'лапинкойра, финнский лаппхунд'), ('лапинпорокойра', 'лапинпорокойра'), ('лапландский шпиц', 'лапландский шпиц'), ('ларри', 'ларри'), ('левеск', 'левеск'), ('левретка, итальянская борзая', 'левретка, итальянская борзая'), ('лёвхен, львиная собачка', 'лёвхен, львиная собачка'), ('лейкланд-терьер', 'лейкланд-терьер'), ('леонбергер', 'леонбергер'), ('леопардовая гончая', 'леопардовая гончая'), ('леопардовая собака катахулы', 'леопардовая собака катахулы'), ('лёрчер', 'лёрчер'), ('литовская гончая', 'литовская гончая'), ('лудогорская гончая', 'лудогорская гончая'), ('лхасский апсо', 'лхасский апсо'), ('люненбургская гончая', 'люненбургская гончая'), ('люцернер лауфхунд', 'люцернер лауфхунд'), ('малая англо-французская гончая', 'малая англо-французская гончая'), ('малый брабансон', 'малый брабансон'), ('малый вандейский бассет-гриффон', 'малый вандейский бассет-гриффон'), ('малый мюнстерлендер', 'малый мюнстерлендер'), ('малый французский брак', 'малый французский брак'), ('мальтез, мальтийский бишон', 'мальтез, мальтийский бишон'), ('манчестерский терьер', 'манчестерский терьер'), ('маратхская борзая', 'маратхская борзая'), ('маремма', 'маремма'), ('мастино наполетано', 'мастино наполетано'), ('медвежья канадская собака талтан', 'медвежья канадская собака талтан'), ('медиу поденгу португезу', 'медиу поденгу португезу'), ('метис', 'метис'), ('микадо терьер', 'микадо терьер'), ('миниатюрный ксолойтцкуинтли', 'миниатюрный ксолойтцкуинтли'), ('мино', 'мино'), ('миттельшнауцер', 'миттельшнауцер'), ('монтебёф', 'монтебёф'), ('мопс', 'мопс'), ('московская сторожевая', 'московская сторожевая'), ('московский длинношерстный той-терьер', 'московский длинношерстный той-терьер'), ('московский дракон', 'московский дракон'), ('московский короткошерстный той-терьер', 'московский короткошерстный той-терьер'), ('мууди', 'мууди'), ('немецкая овчарка', 'немецкая овчарка'), ('немецкая оленегонная лайка', 'немецкая оленегонная лайка'), ('немецкий вахтельхунд', 'немецкий вахтельхунд'), ('немецкий вольфшпиц', 'немецкий вольфшпиц'), ('немецкий дог', 'немецкий дог'), ('немецкий карликовый шпиц', 'немецкий карликовый шпиц'), ('немецкий шпиц', 'немецкий шпиц'), ('нивернейский гриффон', 'нивернейский гриффон'), ('новогвинейская поющая собака', 'новогвинейская поющая собака'), ('новошотландский ретривер', 'новошотландский ретривер'), ('норботтен шпиц', 'норботтен шпиц'), ('норвежский бухунд', 'норвежский бухунд'), ('норвежский дункер хаунд', 'норвежский дункер хаунд'), ('норвежский лундехунд', 'норвежский лундехунд'), ('норвежский элкхаунд', 'норвежский элкхаунд'), ('норвич-терьер', 'норвич-терьер'), ('нормандская гончая', 'нормандская гончая'), ('норфолк терьер', 'норфолк терьер'), ('ньюфаундленд', 'ньюфаундленд'), ('ойразир', 'ойразир'), ('ойуки терьер', 'ойуки терьер'), ('орхидея петербургская', 'орхидея петербургская'), ('оттерхаунд, выдровая гончая', 'оттерхаунд, выдровая гончая'), ('палевый бретонский бассет-гриффо', 'палевый бретонский бассет-гриффо'), ('папильон', 'папильон'), ('паттердейл-терьер', 'паттердейл-терьер'), ('пекинес', 'пекинес'), ('пекиньу поденгу португезу', 'пекиньу поденгу португезу'), ('пердигейру португезу', 'пердигейру португезу'), ('пердигеро де бургос', 'пердигеро де бургос'), ('пердигеро наварро', 'пердигеро наварро'), ('перро де пастор мальоркин', 'перро де пастор мальоркин'), ('перро де преса мальоркин', 'перро де преса мальоркин'), ('перро де пресса канарио', 'перро де пресса канарио'), ('перуанская орхидея инков', 'перуанская орхидея инков'), ('пикардийская овчарка', 'пикардийская овчарка'), ('пинчер', 'пинчер'), ('пинчер миниатюрный', 'пинчер миниатюрный'), ('пиринейская овчарка', 'пиринейская овчарка'), ('пиринейский мастиф', 'пиринейский мастиф'), ('подгальянская овчарка', 'подгальянская овчарка'), ('поденгу ди мастра', 'поденгу ди мастра'), ('поденгу ибисенко, ибисская собака', 'поденгу ибисенко, ибисская собака'), ('польская низинная собака', 'польская низинная собака'), ('польский огар', 'польский огар'), ('помераниан', 'помераниан'), ('померанский шпиц', 'померанский шпиц'), ('понт-одмерский эпаньоль', 'понт-одмерский эпаньоль'), ('порселен, фарфоровая гончая', 'порселен, фарфоровая гончая'), ('посавская гончая', 'посавская гончая'), ('пражский крысарик', 'пражский крысарик'), ('пуатвен, пуатвинская гончая', 'пуатвен, пуатвинская гончая'), ('пудель', 'пудель'), ('пудель миниатюрный', 'пудель миниатюрный'), ('пудель стандартный', 'пудель стандартный'), ('пудель-пойнтер', 'пудель-пойнтер'), ('пули', 'пули'), ('пуми', 'пуми'), ('пшеничный мягкошерстный терьер', 'пшеничный мягкошерстный терьер'), ('рампурская борзая', 'рампурская борзая'), ('растреадор бразилейру', 'растреадор бразилейру'), ('рафейру ду алентежу', 'рафейру ду алентежу'), ('ретривер', 'ретривер'), ('Риджбек', 'Риджбек'), ('ризеншнауцер', 'ризеншнауцер'), ('родезийский риджбек', 'родезийский риджбек'), ('ротвейлер', 'ротвейлер'), ('румынская овчарка', 'румынская овчарка'), ('русская гончая', 'русская гончая'), ('русская пегая гончая', 'русская пегая гончая'), ('русский спаниель', 'русский спаниель'), ('русский той-терьер', 'русский той-терьер'), ('русский черный терьер', 'русский черный терьер'), ('русско-европейская лайка', 'русско-европейская лайка'), ('рэт-терьер', 'рэт-терьер'), ('саарлосвольфхунд', 'саарлосвольфхунд'), ('сабуесо эспаньоле де монте', 'сабуесо эспаньоле де монте'), ('сабуэсо эспаньоль де монте', 'сабуэсо эспаньоль де монте'), ('салюки, персидская гончая', 'салюки, персидская гончая'), ('самоедская лайка', 'самоедская лайка'), ('санин', 'санин'), ('сансю', 'сансю'), ('сегуджио итальяно', 'сегуджио итальяно'), ('сенбернар', 'сенбернар'), ('сен-жерменский брак', 'сен-жерменский брак'), ('серис', 'серис'), ('сеттер-гордон', 'сеттер-гордон'), ('сиба-ину', 'сиба-ину'), ('сибирская хаски', 'сибирская хаски'), ('сибирский хаски', 'сибирский хаски'), ('сийлихам терьер', 'сийлихам терьер'), ('сика ину', 'сика ину'), ('сикоку', 'сикоку'), ('силки терьер', 'силки терьер'), ('синсю', 'синсю'), ('скай терьер', 'скай терьер'), ('скотч терьер', 'скотч терьер'), ('словацкий копов', 'словацкий копов'), ('словацкий чувач', 'словацкий чувач'), ('слюги, арабская борзая', 'слюги, арабская борзая'), ('смаусхонд', 'смаусхонд'), ('смешанная', 'смешанная'), ('смитфильд-колли', 'смитфильд-колли'), ('смоландстёваре, смоландская гончая', 'смоландстёваре, смоландская гончая'), ('солуки', 'солуки'), ('спиноне', 'спиноне'), ('среднеазиатская овчарка', 'среднеазиатская овчарка'), ('средний шнауцер', 'средний шнауцер'), ('средняя англо-французская гончая', 'средняя англо-французская гончая'), ('стабихаун', 'стабихаун'), ('стародатская легавая', 'стародатская легавая'), ('стафордширский бультерьер', 'стафордширский бультерьер'), ('стреллуфстёвер', 'стреллуфстёвер'), ('суоменайокойра, финская гончая', 'суоменайокойра, финская гончая'), ('суоменпастикорва, финский шпиц', 'суоменпастикорва, финский шпиц'), ('суссекс-спаниель', 'суссекс-спаниель'), ('тазы (среднеазиатская борзая)', 'тазы (среднеазиатская борзая)'), ('тай риджбек', 'тай риджбек'), ('тайган, киргизская борзая', 'тайган, киргизская борзая'), ('такса гладкошерстная', 'такса гладкошерстная'), ('такса длинношерстная', 'такса длинношерстная'), ('такса жесткошерстная', 'такса жесткошерстная'), ('такса кроличья', 'такса кроличья'), ('такса миниатюрная', 'такса миниатюрная'), ('такса стандартная', 'такса стандартная'), ('теломиан', 'теломиан'), ('тибетский мастиф', 'тибетский мастиф'), ('тибетский спаниель', 'тибетский спаниель'), ('тибетский терьер', 'тибетский терьер'), ('тирольская гончая', 'тирольская гончая'), ('той-пудель', 'той-пудель'), ('той-терьер', 'той-терьер'), ('тоса ину', 'тоса ину'), ('уест-хайланд-уайт-терьер', 'уест-хайланд-уайт-терьер'), ('уипет', 'уипет'), ('фален, континентальный той-спаниель', 'фален, континентальный той-спаниель'), ('фараоновая собака', 'фараоновая собака'), ('фила бразилейру (бразильский мастиф)', 'фила бразилейру (бразильский мастиф)'), ('фильд спаниель', 'фильд спаниель'), ('финская лайка', 'финская лайка'), ('финский шпиц', 'финский шпиц'), ('фландрский бувье', 'фландрский бувье'), ('фокстерьер гладкошерстный', 'фокстерьер гладкошерстный'), ('фокстерьер жесткошерстный', 'фокстерьер жесткошерстный'), ('французская гончая', 'французская гончая'), ('французский бульдог', 'французский бульдог'), ('французский эпаньоль', 'французский эпаньоль'), ('француский бульдог', 'француский бульдог'), ('фу куок', 'фу куок'), ('халенденстёваре, хальденская гончая', 'халенденстёваре, хальденская гончая'), ('ханаанская собака', 'ханаанская собака'), ('харрьер', 'харрьер'), ('хаски антарктическая', 'хаски антарктическая'), ('ховаварт', 'ховаварт'), ('хорватская овчарка', 'хорватская овчарка'), ('хортая', 'хортая'), ('хюгенхунд', 'хюгенхунд'), ('хюнерхунд', 'хюнерхунд'), ('цвергпинчер', 'цвергпинчер'), ('цвергшнауцер', 'цвергшнауцер'), ('цвергшпиц', 'цвергшпиц'), ('чау-чау', 'чау-чау'), ('черный терьер', 'черный терьер'), ('чесапик бей ретривер', 'чесапик бей ретривер'), ('чехословацкий влчак', 'чехословацкий влчак'), ('чешский терьер', 'чешский терьер'), ('чешский фоусек', 'чешский фоусек'), ('чинук', 'чинук'), ('чихуахуа', 'чихуахуа'), ('чи-хуа-хуа', 'чи-хуа-хуа'), ('шапендус', 'шапендус'), ('шарпей', 'шарпей'), ('шарпланинская овчарка', 'шарпланинская овчарка'), ('швайсхунд', 'швайсхунд'), ('шведский вальхунд', 'шведский вальхунд'), ('швейцарская овчарка', 'швейцарская овчарка'), ('швейцарский лауфхунд', 'швейцарский лауфхунд'), ('шелти', 'шелти'), ('шельти', 'шельти'), ('шиллерстёваре', 'шиллерстёваре'), ('шипперке', 'шипперке'), ('ши-тцу', 'ши-тцу'), ('шотландский дирхаунд', 'шотландский дирхаунд'), ('шотландский терьер', 'шотландский терьер'), ('шпиц', 'шпиц'), ('штихельхаар', 'штихельхаар'), ('Щвейцарский зенненхунд', 'Щвейцарский зенненхунд'), ('энтлебухер зенненхунд', 'энтлебухер зенненхунд'), ('эпаньоль нэн', 'эпаньоль нэн'), ('эрдели копо, трансильванская гончая', 'эрдели копо, трансильванская гончая'), ('эрдельтерьер', 'эрдельтерьер'), ('эскимосская лайка', 'эскимосская лайка'), ('эстонская гончая', 'эстонская гончая'), ('югославская грехцветная гончая', 'югославская грехцветная гончая'), ('южная гончая', 'южная гончая'), ('южнорусская овчарка', 'южнорусская овчарка'), ('ягдтерьер', 'ягдтерьер'), ('японский спаниель', 'японский спаниель'), ('японский стерьер', 'японский стерьер'), ('японский хин', 'японский хин'), ('японский шпиц ', 'японский шпиц ')], default='метис', help_text='Порода', max_length=50, verbose_name='Порода'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='color',
            field=models.CharField(choices=[('светло коричневый', 'светло коричневый'), ('черепаховый', 'черепаховый'), ('красный', 'красный'), ('дымчатый', 'дымчатый'), ('перец с солью', 'перец с солью'), ('абрикосовый', 'абрикосовый'), ('кремовый', 'кремовый'), ('голубой с белым', 'голубой с белым'), ('голубой с пятнами', 'голубой с пятнами'), ('палевый', 'палевый'), ('чалый', 'чалый'), ('голубой  с подпалом', 'голубой  с подпалом'), ('пегий', 'пегий'), ('биколор (черный/красный)', 'биколор (черный/красный)'), ('дымчатый золотистый', 'дымчатый золотистый'), ('черный', 'черный'), ('темно коричневый', 'темно коричневый'), ('соболиный', 'соболиный'), ('рыжий', 'рыжий'), ('триколор (красный/черный/лиловый)', 'триколор (красный/черный/лиловый)'), ('золотой', 'золотой'), ('серебристый', 'серебристый'), ('фавн (бежевый)', 'фавн (бежевый)'), ('черно-белый', 'черно-белый'), ('голубой', 'голубой'), ('коричневый', 'коричневый'), ('шиншилла', 'шиншилла'), ('красный с белым', 'красный с белым'), ('молочный', 'молочный'), ('волчий', 'волчий'), ('тигровый', 'тигровый'), ('черный с белым', 'черный с белым'), ('лиловый с белым', 'лиловый с белым'), ('арлекин', 'арлекин'), ('бледно-желтый', 'бледно-желтый'), ('светло-коричневый', 'светло-коричневый'), ('черно-красный-белый', 'черно-красный-белый'), ('биколор', 'биколор'), ('мраморный', 'мраморный'), ('муругий', 'муругий'), ('белый', 'белый'), ('циннамон (корица)', 'циннамон (корица)'), ('лиловый', 'лиловый'), ('чепрачный', 'чепрачный'), ('голубо-кремовый черепаховый', 'голубо-кремовый черепаховый'), ('шоколадный', 'шоколадный')], default='черный', help_text='Цвет', max_length=50, verbose_name='Цвет'),
        ),
    ]