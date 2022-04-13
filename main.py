@namespace
class SpriteKind:
    item = SpriteKind.create()
    doubleshoot = SpriteKind.create()
    ultraattack = SpriteKind.create()
    explosion = SpriteKind.create()
    fireball = SpriteKind.create()
    boss = SpriteKind.create()
    bossfire = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    MEGAattack.set_position(34, 5)
    MEGAattack.lifespan = 5000
sprites.on_overlap(SpriteKind.player, SpriteKind.ultraattack, on_on_overlap)

def music3():
    if Math.percent_chance(33.3):
        music.play_melody("C5 A B D G E F C ", 120)
    if Math.percent_chance(33.3):
        music.play_melody("G A B F G E F C ", 120)
    if Math.percent_chance(33.3):
        music.play_melody("G B A G C5 B A B ", 120)
    if Math.percent_chance(33.3):
        music.play_melody("C5 A B G A F G E ", 120)
    if Math.percent_chance(33.3):
        music.play_melody("E D G F B A C5 B ", 120)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_life_by(-1)
    otherSprite2.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.bossfire, on_on_overlap2)

def on_a_pressed():
    global projectile, explosion2
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 2 . . . . . . . . 
                    . . . . . . . 2 . . . . . . . . 
                    . . . . . . . 2 . . . . . . . . 
                    . . . . . . . 2 . . . . . . . . 
                    . . . . . . . 2 . . . . . . . . 
                    . . . . . . . 2 . . . . . . . . 
                    . . . . . . . 2 . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        mySprite,
        0,
        -50)
    if MEGAattack and MEGAattack.lifespan > 0:
        explosion2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . 2 1 2 . . . . . . 
                            . . . . . . . 2 1 2 . . . . . . 
                            . . . . . . . 2 1 2 . . . . . . 
                            . . . . . . . 3 1 3 . . . . . . 
                            . . . . . . 2 3 1 3 2 . . . . . 
                            . . . . . . 2 1 1 1 2 . . . . . 
                            . . . . . . 2 1 1 1 3 . . . . . 
                            . . . . . . 3 1 1 1 3 . . . . . 
                            . . . . . . 3 1 1 1 3 . . . . . 
                            . . . . . . 3 1 1 1 3 . . . . . 
                            . . . . . . 2 3 1 3 2 . . . . . 
                            . . . . . . . 2 2 2 . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.explosion)
        explosion2.lifespan = 10000
        scaling.scale_by_pixels(explosion2, 30, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
        explosion2.set_position(randint(10, 150), randint(10, 110))
        animation.run_image_animation(explosion2,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . 2 1 2 . . . . . . 
                                . . . . . . . 2 1 2 . . . . . . 
                                . . . . . . . 2 1 2 . . . . . . 
                                . . . . . . . 3 1 3 . . . . . . 
                                . . . . . . 2 3 1 3 2 . . . . . 
                                . . . . . . 2 1 1 1 2 . . . . . 
                                . . . . . . 2 1 1 1 3 . . . . . 
                                . . . . . . 3 1 1 1 3 . . . . . 
                                . . . . . . 3 1 1 1 3 . . . . . 
                                . . . . . . 3 1 1 1 3 . . . . . 
                                . . . . . . 2 3 1 3 2 . . . . . 
                                . . . . . . . 2 2 2 . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . 2 3 3 3 3 3 2 . . . . 
                                . . . . 3 1 1 1 1 1 1 1 3 . . . 
                                . . . . 1 1 1 1 1 1 1 1 1 . . . 
                                . . . 2 1 1 1 1 1 1 1 1 1 2 . . 
                                . . . 2 3 1 1 1 1 1 1 3 3 2 . . 
                                . . . . . . 2 2 2 2 2 . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . 4 4 4 4 4 . . . . . . 
                                . . . 4 4 4 5 5 5 d 4 4 4 4 . . 
                                . . 4 d 5 d 5 5 5 d d d 4 4 . . 
                                . . 4 5 5 1 1 1 d d 5 5 5 4 . . 
                                . 4 5 5 5 1 1 1 5 1 1 5 5 4 4 . 
                                . 4 d d 1 1 5 5 5 1 1 5 5 d 4 . 
                                . 4 5 5 1 1 5 1 1 5 5 d d d 4 . 
                                . 2 5 5 5 d 1 1 1 5 1 1 5 5 2 . 
                                . 2 d 5 5 d 1 1 1 5 1 1 5 5 2 . 
                                . . 2 4 d d 5 5 5 5 d d 5 4 . . 
                                . . . 2 2 4 d 5 5 d d 4 4 . . . 
                                . . 2 2 2 2 2 4 4 4 2 2 2 . . . 
                                . . . 2 2 4 4 4 4 4 4 2 2 . . . 
                                . . . . . 2 2 2 2 2 2 . . . . .
                """),
                img("""
                    . . . . 2 2 2 2 2 2 2 2 . . . . 
                                . . . 2 4 4 4 5 5 4 4 4 2 2 2 . 
                                . 2 2 5 5 d 4 5 5 5 4 4 4 4 2 . 
                                . 2 4 5 5 5 5 d 5 5 5 4 5 4 2 2 
                                . 2 4 d d 5 5 5 5 5 5 d 4 4 4 2 
                                2 4 5 5 d 5 5 5 d d d 5 5 5 4 4 
                                2 4 5 5 4 4 4 d 5 5 d 5 5 5 4 4 
                                4 4 4 4 . . 2 4 5 5 . . 4 4 4 4 
                                . . b b b b 2 4 4 2 b b b b . . 
                                . b d d d d 2 4 4 2 d d d d b . 
                                b d d b b b 2 4 4 2 b b b d d b 
                                b d d b b b b b b b b b b d d b 
                                b b d 1 1 3 1 1 d 1 d 1 1 d b b 
                                . . b b d d 1 1 3 d d 1 b b . . 
                                . . 2 2 4 4 4 4 4 4 4 4 2 2 . . 
                                . . . 2 2 4 4 4 4 4 2 2 2 . . .
                """),
                img("""
                    . . . . . . . . b b . . . . . . 
                                . . . . . . . . b b . . . . . . 
                                . . . b b b . . . . . . . . . . 
                                . . b d d b . . . . . . . b b . 
                                . b d d d b . . . . . . b d d b 
                                . b d d b . . . . b b . b d d b 
                                . b b b . . . . . b b . . b b . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . b b b d d d d d d b b b . . 
                                . b d c c c b b b b c c d d b . 
                                b d d c b . . . . . b c c d d b 
                                c d d b b . . . . . . b c d d c 
                                c b d d d b b . . . . b d d c c 
                                . c c b d d d d b . c c c c c c 
                                . . . c c c c c c . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """)],
            200,
            False)
        music.big_crash.play_until_done()
        scene.camera_shake(8, 500)
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy, effects.fire, 1000)
    if info.score() >= 222:
        projectile.x += -5
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 2 . . . . . . . . 
                            . . . . . . . 2 . . . . . . . . 
                            . . . . . . . 2 . . . . . . . . 
                            . . . . . . . 2 . . . . . . . . 
                            . . . . . . . 2 . . . . . . . . 
                            . . . . . . . 2 . . . . . . . . 
                            . . . . . . . 2 . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            0,
            -50)
        projectile.x += 7
    projectile.set_kind(SpriteKind.projectile)
    music.pew_pew.play()
    pause(100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap3(sprite3, otherSprite3):
    info.change_life_by(1)
    otherSprite3.set_position(0, 0)
    music.magic_wand.play_until_done()
sprites.on_overlap(SpriteKind.player, SpriteKind.item, on_on_overlap3)

def on_on_zero(status):
    Boss1.destroy(effects.fire, 500)
    music.beam_up.play_until_done()
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

def on_on_overlap4(sprite4, otherSprite4):
    statusbar.value += -5
    sprite4.destroy()
sprites.on_overlap(SpriteKind.projectile, SpriteKind.boss, on_on_overlap4)

def bosshootboi():
    global bossprojectile
    for index in range(50):
        bossprojectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 2 2 . . . . . . . 
                            . . . . . . 3 1 1 3 . . . . . . 
                            . . . . . 2 1 1 1 1 2 . . . . . 
                            . . . . . 2 1 1 1 1 2 . . . . . 
                            . . . . . . 3 1 1 3 . . . . . . 
                            . . . . . . . 2 2 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            Boss1,
            0,
            50)
        bossprojectile.set_kind(SpriteKind.bossfire)
        pause(800)

def on_on_overlap5(sprite5, otherSprite5):
    global item2, MEGAattack
    info.change_score_by(1)
    sprite5.destroy()
    otherSprite5.destroy(effects.disintegrate, 500)
    if Math.percent_chance(5):
        item2 = sprites.create(img("""
                ....................
                            ....................
                            ....................
                            ....................
                            ....................
                            ....................
                            .......22...22......
                            ......2322.2222.....
                            ......232222222.....
                            ......222222222.....
                            .......22222b2......
                            ........222b2.......
                            .........222........
                            ..........2.........
                            ....................
                            ....................
                            ....................
                            ....................
                            ....................
                            ....................
            """),
            SpriteKind.item)
        item2.set_position(otherSprite5.x, otherSprite5.y)
        item2.lifespan = 5000
    if Math.percent_chance(0.5):
        MEGAattack = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . f f f f f f f . . . . . 
                            . . . f f f f f f f f f . . . . 
                            . . f f f f f f f f f f f . . . 
                            . f f f 2 2 f f f 2 2 f f f . . 
                            . f f f 2 f 2 f 2 f 2 f f f . . 
                            . f f f 2 f f 2 f f 2 f f f . . 
                            . f f f 2 f f f f f 2 f f f . . 
                            . f f f 2 f f f f f 2 f f f . . 
                            . f f f 2 f f f f f 2 f f f . . 
                            . f f f 2 f f f f f 2 f f f . . 
                            . . f f f f f f f f f f f . . . 
                            . . . f f f f f f f f f . . . . 
                            . . . . f f f f f f f . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.ultraattack)
        MEGAattack.set_position(otherSprite5.x, otherSprite5.y)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap5)

def music2():
    if Math.percent_chance(33.3):
        music.play_melody("C5 A E D G A F C ", 120)
    if Math.percent_chance(33.3):
        music.play_melody("G A F B D E F C ", 120)
    if Math.percent_chance(33.3):
        music.play_melody("G B F G C5 E G B ", 120)
    if Math.percent_chance(33.3):
        music.play_melody("C5 A B G A F G E ", 120)
    if Math.percent_chance(33.3):
        music.play_melody("F F E D G F A G ", 120)

def on_on_overlap6(sprite6, otherSprite6):
    info.change_life_by(-1)
    scene.camera_shake(6, 500)
    music.zapped.play_until_done()
    pause(286)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap6)

spawn = 0
rocks: Sprite = None
item2: Sprite = None
bossprojectile: Sprite = None
statusbar: StatusBarSprite = None
Boss1: Sprite = None
explosion2: Sprite = None
projectile: Sprite = None
MEGAattack: Sprite = None
mySprite: Sprite = None
mySprite = sprites.create(img("""
        .....................
            .....................
            .....................
            .....................
            .....................
            .....................
            .....................
            .....................
            .....................
            .....................
            .....................
            .....................
            ..........11.........
            .........1111........
            .........1111........
            ........119911.......
            ........199991.......
            ........199991.......
            ........119911.......
            ........111111.......
            ........111111.......
            ........111111.......
            .......21111112......
            ......2211111122.....
            .....222111111222....
            ....22221111112222...
            .........1111........
            ........455555.......
            ........455555.......
            ........545552.......
            .........5452........
            .........2555........
            ..........255........
            ..........45.........
            ...........4.........
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
effects.star_field.start_screen_effect()
mySprite.set_position(80, 97)
info.set_score(50)
info.set_life(5)
enemyspeed = 45
game.splash("Space invaders 2022 ")
game.set_dialog_frame(img("""
    ..................................................................
        ............fff........fff.............fff..............ffff......
        ...........fddbf......fbdbf...........fbdbf............fbddf......
        ...........fddbbf.....fdddffff........fdddffff...fff..ffddbff.....
        ...........fddddffffffbdddbddbffffffffbdddbddbffffddffddddddf.....
        ...fff....fdddddfddddddddbbddddddddddddddbbddddddfdddddbccddf.....
        .fffddf..fddffffddddddddddbbddddddddddddddbbdddddffbddbbddff......
        .fdbddfffddfffdddfffffbdddbddbffffffffbdddbddbfffefddccbddf.......
        .fdddcddddffeffffeeeeefbdbfddfeeeeeeeefbdbfddfeeeefffcddddf.......
        .fbddcddddfeeeeeeeeeeeefffffffeeeeeeeeefffffffeeeeeeefdddddf......
        ..ffdbbbddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffddf.....
        ...fddbcddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffddfff..
        ....fddccffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffddddf.
        ....fdddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffddddf.
        ...fddbdfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdfddbbf.
        ...fddfffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdfddbf..
        ...ffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddfff...
        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
        ...fbddbffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
        ...fdddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
        ...fddbddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbddbff..
        ..ffbbbbffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbdddddbf.
        .fbddbddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddddf.
        .fdddddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbddbddbf.
        .fbdddddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffbbbbff..
        ..ffbddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddbddf...
        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddf...
        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffbddbf...
        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
        ...fbddbffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
        ...fdddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
        ...fddbddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbddbff..
        ..ffbbbbffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbdddddbf.
        .fbddbddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddddf.
        .fdddddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbddbddbf.
        .fbdddddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffbbbbff..
        ..ffbddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddbddf...
        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddf...
        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffbddbf...
        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
        ...fffddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffff...
        ..fbddfdfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffddf...
        .fbbddfdfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdbddf...
        .fddddfffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddf....
        .fddddffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffccddf....
        ..fffddffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddcbddf...
        .....fddfffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddbbbdff..
        ......fdddddfeeeeeeefffffffeeeeeeeeefffffffeeeeeeeeeeeefddddcddbf.
        .......fddddcfffeeeefddfbdbfeeeeeeeefddfbdbfeeeeeffffeffddddcdddf.
        .......fddbccddfefffbddbdddbffffffffbddbdddbfffffdddfffddfffddbdf.
        ......ffddbbddbffdddddbbddddddddddddddbbddddddddddffffddf..fddfff.
        .....fddccbdddddfddddddbbddddddddddddddbbddddddddfdddddf....fff...
        .....fddddddffddffffbddbdddbffffffffbddbdddbffffffddddf...........
        .....ffbddff..fff...ffffdddf........ffffdddf.....fbbddf...........
        ......fddbf............fbdbf...........fbdbf......fbddf...........
        ......ffff..............fff.............fff........fff............
        ..................................................................
"""))
game.show_long_text("Beta 1.0                -made boss one randomly spawn between 80 and 120                      -fixed bug #3",
    DialogLayout.FULL)
game.set_dialog_frame(img("""
    ...cc..............................cc.....
        ..c55c..bbbb...bbbbb...bbbbb......c55c....
        .cb55bcbdddbbbbbdddbbbbbdddbbbbbbcb55bc...
        b555555bbdddb111bdddb111bdddb11db555555b..
        bb5555bbbbdb11111bdb11111bdb1111bb5555bb..
        cb5555bcddd11111ddd11111ddd11111cb5555bc..
        .c5bb5c1111d111d111d111d111d111ddc5bb5c...
        .cbbbbc11111111111111111111111111cbbbbc...
        ..b1111111111111111111111111111111dddbb...
        ..b11111111111111111111111111111111dbbdb..
        ..bb1111111111111111111111111111111dbddb..
        .bbdb1d1111111111111111111111111111ddddb..
        .bdddd1111111111111111111111111111d1bdbb..
        .bddbd1111111111111111111111111111111bb...
        .bdb1d11111111111111111111111111111111b...
        .bb111d1111111111111111111111111111111b...
        ..b1111111111111111111111111111111d111bb..
        ..b11111111111111111111111111111111d1bdb..
        ..bb1111111111111111111111111111111dbddb..
        .bbdb1d1111111111111111111111111111ddddb..
        .bdddd1111111111111111111111111111d1bdbb..
        .bddbd1111111111111111111111111111111bb...
        .bdb1d11111111111111111111111111111111b...
        .bb111d1111111111111111111111111111111b...
        ..b1111111111111111111111111111111d111bb..
        ..b11111111111111111111111111111111d1bdb..
        ..bb1111111111111111111111111111111dbddb..
        .bbdb1d1111111111111111111111111111ddddb..
        .bdddd1111111111111111111111111111d1bdbb..
        .bddbd1111111111111111111111111111111bb...
        .bdbb111111111111111111111111111111111b...
        .bbbd111111111111111111111111111111111b...
        ..bcc11111111111111111111111111111dccdb...
        ..c55c1111111d111d111d111d111d1111c55cb...
        .cb55bcdd11111ddd11111ddd11111dddcb55bc...
        b555555bd1111bdb11111bdb11111bdbb555555b..
        bb5555bbdd11bdddb111bdddb111bdddbb5555bb..
        cb5555bcbbbbbbdddbbbbbdddbbbbbddcb5555bc..
        .c5bb5c......bbbbb...bbbbb...bbbbc5bb5c...
        .cbbbbc..........................cbbbbc...
        ..........................................
        ..........................................
"""))
game.show_long_text("Welcome to space defenders! slay enemies with lasers using the button \"A\", and get as far as you can. Good luck adventurer!",
    DialogLayout.FULL)
mySprite.set_stay_in_screen(True)

def on_forever():
    global rocks
    rocks = sprites.create(img("""
            . . . . . . . . . c c 8 . . . . 
                    . . . . . . 8 c c c f 8 c c . . 
                    . . . c c 8 8 f c a f f f c c . 
                    . . c c c f f f c a a f f c c c 
                    8 c c c f f f f c c a a c 8 c c 
                    c c c b f f f 8 a c c a a a c c 
                    c a a b b 8 a b c c c c c c c c 
                    a f c a a b b a c c c c c f f c 
                    a 8 f c a a c c a c a c f f f c 
                    c a 8 a a c c c c a a f f f 8 a 
                    . a c a a c f f a a b 8 f f c a 
                    . . c c b a f f f a b b c c 6 c 
                    . . . c b b a f f 6 6 a b 6 c . 
                    . . . c c b b b 6 6 a c c c c . 
                    . . . . c c a b b c c c . . . . 
                    . . . . . c c c c c c . . . . .
        """),
        SpriteKind.enemy)
    rocks.set_position(randint(10, 120), randint(0, 0))
    rocks.set_velocity(5, enemyspeed)
    rocks.lifespan = 10000
    pause(spawn)
forever(on_forever)

def on_forever2():
    if info.score() >= 0:
        music2()
    if info.score() >= 200:
        music3()
forever(on_forever2)

def on_forever3():
    global Boss1, statusbar
    if info.score() == 100:
        Boss1 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . f f f f . . . . . . 
                            . . . . . f 9 9 9 9 f . . . . . 
                            . . . . f 9 1 1 9 9 9 f . . . . 
                            . . . . f 9 1 1 9 9 9 f . . . . 
                            . . . . f 9 9 9 9 9 9 f . . . . 
                            . . . . f 9 9 9 9 9 9 f . . . . 
                            . . . . f 9 9 9 9 9 9 f . . . . 
                            . . f f f f f f f f f f f f . . 
                            . f c c c c c c c c c c c c f . 
                            . f c c c c c c c c c c c c f . 
                            . . f f f c c c c c c f f f . . 
                            . . . . . f f f f f f . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.boss)
        scaling.scale_by_pixels(Boss1, 30, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
        Boss1.set_position(80, 40)
        game.set_dialog_frame(img("""
            .....cccccccccccccc.....
                        ...cbd111111111111dbc...
                        ..cd1111111111111111dc..
                        .cd111111111111111111dc.
                        .b11111111111111111111b.
                        cd11111111111111111111dc
                        c1111111111111111111111c
                        c1111111111111111111111c
                        c1111111111111111111111c
                        c1111111111111111111111c
                        c1111111111111111111111c
                        c1111111111111111111111c
                        c1111111111111111111111c
                        c1111111111111111111111c
                        c1111111111111111111111c
                        c1111111111111111111111c
                        cd11111111111111111111dc
                        cb11111111111111111111bc
                        ccd111111111111111111dc.
                        .ccd1111111111111111dcc.
                        ..c111111111111111dbcc..
                        .b11dcccccccccccccccc...
                        cddcccccccccccccccc.....
                        ccccc...................
        """))
        game.show_long_text("You may be this far but I won't let you save the princess...!",
            DialogLayout.FULL)
        Boss1.vx = 50
        Boss1.vy = 0
        Boss1.set_bounce_on_wall(True)
        statusbar = statusbars.create(25, 4, StatusBarKind.enemy_health)
        statusbar.max = 100
        statusbar.value = 100
        statusbar.attach_to_sprite(Boss1, -5, 0)
        info.set_life(10)
        bosshootboi()
        info.change_score_by(1)
forever(on_forever3)

def on_update_interval():
    global enemyspeed, spawn
    enemyspeed += 1
    enemyspeed = min(enemyspeed, 70)
    spawn = 1000
    spawn += -50
    spawn = min(spawn, 600)
game.on_update_interval(10000, on_update_interval)
