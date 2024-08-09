Player.getInteractionManager().interact()

JsMacros.once('SignEdit',true,JavaWrapper.methodToJava((e) => {
    e.closeScreen = true;
    e.signText[0] = 'sand';
}));