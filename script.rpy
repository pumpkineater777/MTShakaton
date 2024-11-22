define teller = Character("", color="ffffff")
define garry = Character("Гарри", color="aaa8a7")
define hagrid = Character("Хагрид", color="9c7044")
define olivander = Character("Оливандер", color="9c7044")
define villain = Character("Воландеморт", color="eb0a0a")

image hall = "images/hall.png"
image hall_damaged = "images/hall_damaged.png"
image hagrid = "images/hagrid.png"
image school = "images/school.png"
image vollandemort = "images/vollandemort.png"
image vollandemort_kill = "images/vollandemort_kill.png"
image wand_shop = "images/wand_shop.png"
image olivander = "images/olivander.png"
image shampur = "images/shampur.png"
image normal_wand = "images/normal_wand.png"
image self_harm_wand = "images/self_harm_wand.png"

label start:

    play music "<from 10>music/581.mp3"

    show hall

    teller "Это был обычный, ничем не примечательный день, как появился {b}ОН{/b}"

    show hall_damaged

    play sound "sounds/padenie-kuchi-razlichnyih-predmetov-26438.mp3" volume(0.5)
    show hagrid with vpunch
    hagrid "Фухх, мягкая посадка"
    
    hagrid "Здраствуй Гарри. Я Хагрид"

    garry "Простите, но кто вы?"

    hagrid "Я лесничий при школе Хогвартс"
    hagrid "Гарри, ты волшебник."
    hagrid "Поехали в Хогвартс"

    menu:
        "Юху, ура, Хогвартс":
            hagrid "Отлично, но каждому волшебнику в Хогвратсе непременно нужна волшебная палочка"
            hagrid "Насколько я понимаю, у тебя ее нет, поэтому заедем за палочкой к Оливандеру"
            hide hagrid
            hide hall
            jump pick_magic_wand
        "Не, я обычный ребенок, вы ошиблись":
            hagrid "Я уважаю личность, даже в детях, поэтому смирюсь с твоим выбором"
            hagrid "Ну ладно, прощай"
            hide hagrid
            hide hall
            jump non_magic_ending

    return


label pick_magic_wand:
    show wand_shop with fade

    show olivander

    olivander "Такая честь, что сам Гарри Поттер будет покупать у меня палочку"

    olivander "Сейчас в магазине есть ассортимент из трёх палочек"
    hide olivander
    show shampur at left with dissolve
    olivander "Одна сделана в кузнице в Грузии, сердцевина из дамасской стали"
    show self_harm_wand at right with dissolve
    olivander "Единственная в своем роде палочка полностью из металла"
    show normal_wand at center with dissolve
    olivander "Ооо, эта палочка крайне особенная. Она сделана из древнего дуба, внутри нее волос из хвоста единорога"

    menu:
        "Палочка из Грузии с сердцевиной из дамасской стали":
            pass
        "Дубовая палочка с сердцевиной из хвоста единорога":
            pass
        "Металлическая палочка":
            pass

    hide shampur
    hide normal_wand
    hide self_harm_wand
    show olivander

    olivander "Отличный выбор."

    return

label non_magic_ending:
    show school with fade

    teller "Прошло 5 лет, для Гарри это был обычный день в Лондонской школе"

    show vollandemort with dissolve

    villain "Я убью тебя Гарри, пусть ты и не маг"

    show vollandemort_kill with hpunch

    villain "АВАДА КЕДДАБРА!!!"

    show final with dissolve

    teller "Гарри Поттер умер. Маги всего мира после этой новости стали терять надежду на победу в войне против Воландеморта"
    teller "Воландеморт еще долго держал мир в своей власти"

    return
