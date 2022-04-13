namespace SpriteKind {
    export const item = SpriteKind.create()
    export const doubleshoot = SpriteKind.create()
    export const ultraattack = SpriteKind.create()
    export const explosion = SpriteKind.create()
    export const fireball = SpriteKind.create()
    export const boss = SpriteKind.create()
    export const bossfire = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.ultraattack, function (sprite, otherSprite) {
    MEGAattack.setPosition(34, 5)
    MEGAattack.lifespan = 5000
})
function music3 () {
    if (Math.percentChance(33.3)) {
        music.playMelody("C5 A B D G E F C ", 120)
    }
    if (Math.percentChance(33.3)) {
        music.playMelody("G A B F G E F C ", 120)
    }
    if (Math.percentChance(33.3)) {
        music.playMelody("G B A G C5 B A B ", 120)
    }
    if (Math.percentChance(33.3)) {
        music.playMelody("C5 A B G A F G E ", 120)
    }
    if (Math.percentChance(33.3)) {
        music.playMelody("E D G F B A C5 B ", 120)
    }
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.boss, function (sprite4, otherSprite4) {
    statusbar.value += -5
    sprite4.destroy()
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite5, otherSprite5) {
    info.changeScoreBy(1)
    sprite5.destroy()
    otherSprite5.destroy(effects.disintegrate, 500)
    if (Math.percentChance(5)) {
        item2 = sprites.create(img`
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
            `, SpriteKind.item)
        item2.setPosition(otherSprite5.x, otherSprite5.y)
        item2.lifespan = 5000
    }
    if (Math.percentChance(0.5)) {
        MEGAattack = sprites.create(img`
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
            `, SpriteKind.ultraattack)
        MEGAattack.setPosition(otherSprite5.x, otherSprite5.y)
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, mySprite, 0, -50)
    if (MEGAattack && MEGAattack.lifespan > 0) {
        explosion2 = sprites.create(img`
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
            `, SpriteKind.explosion)
        explosion2.lifespan = 10000
        scaling.scaleByPixels(explosion2, 30, ScaleDirection.Uniformly, ScaleAnchor.Middle)
        explosion2.setPosition(randint(10, 150), randint(10, 110))
        animation.runImageAnimation(
        explosion2,
        [img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `,img`
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
            `],
        200,
        false
        )
        music.bigCrash.playUntilDone()
        scene.cameraShake(8, 500)
        sprites.destroyAllSpritesOfKind(SpriteKind.Enemy, effects.fire, 1000)
    }
    if (info.score() >= 222) {
        projectile.x += -5
        projectile = sprites.createProjectileFromSprite(img`
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
            `, mySprite, 0, -50)
        projectile.x += 7
    }
    projectile.setKind(SpriteKind.Projectile)
    music.pewPew.play()
    pause(100)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite6, otherSprite6) {
    info.changeLifeBy(-1)
    scene.cameraShake(6, 500)
    music.zapped.playUntilDone()
    pause(286)
})
statusbars.onZero(StatusBarKind.EnemyHealth, function (status) {
    Boss1.destroy(effects.fire, 500)
    music.beamUp.playUntilDone()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.item, function (sprite3, otherSprite3) {
    info.changeLifeBy(1)
    otherSprite3.setPosition(0, 0)
    music.magicWand.playUntilDone()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.bossfire, function (sprite2, otherSprite2) {
    info.changeLifeBy(-1)
    otherSprite2.destroy()
})
function bosshootboi () {
    for (let index = 0; index < 50; index++) {
        bossprojectile = sprites.createProjectileFromSprite(img`
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
            `, Boss1, 0, 50)
        bossprojectile.setKind(SpriteKind.bossfire)
        pause(800)
    }
}
function music2 () {
    if (Math.percentChance(33.3)) {
        music.playMelody("C5 A E D G A F C ", 120)
    }
    if (Math.percentChance(33.3)) {
        music.playMelody("G A F B D E F C ", 120)
    }
    if (Math.percentChance(33.3)) {
        music.playMelody("G B F G C5 E G B ", 120)
    }
    if (Math.percentChance(33.3)) {
        music.playMelody("C5 A B G A F G E ", 120)
    }
    if (Math.percentChance(33.3)) {
        music.playMelody("F F E D G F A G ", 120)
    }
}
let spawn = 0
let rocks: Sprite = null
let bossprojectile: Sprite = null
let Boss1: Sprite = null
let explosion2: Sprite = null
let projectile: Sprite = null
let item2: Sprite = null
let statusbar: StatusBarSprite = null
let MEGAattack: Sprite = null
let mySprite: Sprite = null
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 100)
effects.starField.startScreenEffect()
mySprite.setPosition(80, 97)
info.setScore(0)
info.setLife(5)
let enemyspeed = 45
game.splash("Space invaders 2022 ")
game.setDialogFrame(img`
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
    `)
game.showLongText("Beta 1.0                -made boss one randomly spawn between 80 and 120                      -fixed bug #3", DialogLayout.Full)
game.setDialogFrame(img`
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
    `)
game.showLongText("Welcome to space defenders! slay enemies with lasers using the button \"A\", and get as far as you can. Good luck adventurer!", DialogLayout.Full)
mySprite.setStayInScreen(true)
forever(function () {
    rocks = sprites.create(img`
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
        `, SpriteKind.Enemy)
    rocks.setPosition(randint(10, 120), randint(0, 0))
    rocks.setVelocity(5, enemyspeed)
    rocks.lifespan = 10000
    pause(spawn)
})
forever(function () {
    if (info.score() >= 0) {
        music2()
    }
    if (info.score() >= 200) {
        music3()
    }
})
forever(function () {
    if (info.score() == 100) {
        Boss1 = sprites.create(img`
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
            `, SpriteKind.boss)
        scaling.scaleByPixels(Boss1, 30, ScaleDirection.Uniformly, ScaleAnchor.Middle)
        Boss1.setPosition(80, 40)
        game.setDialogFrame(img`
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
            `)
        game.showLongText("You may be this far but I won't let you save the princess...!", DialogLayout.Full)
        Boss1.vx = 50
        Boss1.vy = 0
        Boss1.setBounceOnWall(true)
        statusbar = statusbars.create(25, 4, StatusBarKind.EnemyHealth)
        statusbar.max = 100
        statusbar.value = 100
        statusbar.attachToSprite(Boss1, -5, 0)
        info.setLife(10)
        bosshootboi()
        info.changeScoreBy(1)
    }
})
game.onUpdateInterval(10000, function () {
    enemyspeed += 1
    enemyspeed = Math.min(enemyspeed, 70)
    spawn = 1000
    spawn += -50
    spawn = Math.min(spawn, 600)
})
