<?xml version="1.0" encoding="UTF-8" ?>
<Package name="STT with Django Integration" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="Reply" src="Reply/Reply.dlg" />
    </Dialogs>
    <Resources>
        <File name="icon" src="icon.png" />
        <File name="demo" src="html/index.html" />
    </Resources>
    <Topics>
        <Topic name="Reply_enu" src="Reply/Reply_enu.top" topicName="Reply" language="en_US" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
