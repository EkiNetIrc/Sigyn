###
# Copyright (c) 2016, Nicolas Coevoet
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.conf as conf
import supybot.registry as registry
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('Sigyn')
except:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x:x

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Sigyn', True)


Sigyn = conf.registerPlugin('Sigyn')

conf.registerGlobalValue(Sigyn, 'enable',
     registry.Boolean(False, """set to True to enable kill and klines, otherwise bot will only report to logChannel"""))

conf.registerGlobalValue(Sigyn, 'logChannel',
     registry.String("", """channel where bot's actions is announced"""))
conf.registerGlobalValue(Sigyn, 'useNotice',
     registry.Boolean(False, """use notices for announces in logChannel"""))
     
conf.registerGlobalValue(Sigyn,'resolverTimeout',
    registry.PositiveInteger(3, """max duration of dns request/resolve in seconds"""))
     
conf.registerGlobalValue(Sigyn, 'klineDuration',
     registry.Integer(-1, """kline duration, in minutes, with -1, bot will not kill or kline"""))
conf.registerGlobalValue(Sigyn, 'klineMessage',
     registry.String("Merci de ne pas spammer les utilisateurs d'EkiNetIrc. En cas d'erreur, contactez kline@ekinetirc.com.", """default reason used in kline's message"""))
conf.registerChannelValue(Sigyn, 'killMessage',
     registry.String("Le spam est interdit sur EkiNetIrc", """kill reason"""))
     
conf.registerGlobalValue(Sigyn, 'operatorNick',
     registry.String("", """oper's nick, must be filled""", private=True))
conf.registerGlobalValue(Sigyn, 'operatorPassword',
     registry.String("", """oper's password, must be filled""", private=True))

conf.registerGlobalValue(Sigyn, 'alertPeriod',
    registry.PositiveInteger(1,"""interval between 2 alerts of same type in logChannel"""))
conf.registerGlobalValue(Sigyn, 'netsplitDuration',
    registry.PositiveInteger(1,"""duration of netsplit ( which disable some protections )"""))

conf.registerGlobalValue(Sigyn, 'alertOnWideKline',
    registry.Integer(-1,"""alert if a kline hits more than expected users"""))

conf.registerGlobalValue(Sigyn, 'lagPermit',
     registry.Integer(-1, """max lag allowed in seconds, otherwise entering netsplit mode"""))
conf.registerGlobalValue(Sigyn, 'lagInterval',
     registry.PositiveInteger(1, """interval between two check about lag, also used to garbage collect useless items in internal state"""))

conf.registerGlobalValue(Sigyn, 'ghostPermit',
     registry.Integer(-1, """max number of ghost connections allowed"""))

conf.registerChannelValue(Sigyn, 'eirDuration',
     registry.String("", """eir dnv duration"""))

# sasl abuses detection

conf.registerGlobalValue(Sigyn, 'saslPermit',
    registry.Integer(-1,"""number of sasl attempts allowed during saslLife, -1 to disable"""))
conf.registerGlobalValue(Sigyn, 'saslLife', 
    registry.PositiveInteger(1,"""life of sasl attempts in memory (seconds)"""))
conf.registerGlobalValue(Sigyn, 'saslDuration',
    registry.PositiveInteger(1,"""duration of DLine in minutes"""))
conf.registerGlobalValue(Sigyn, 'saslChannel',
    registry.String("","""channel where sasl attempts are send"""))
conf.registerGlobalValue(Sigyn, 'saslNick',
    registry.String("","""nick who send sasl informations"""))
conf.registerGlobalValue(Sigyn, 'saslReason',
    registry.String("Banned due to too many failed login attempts (SASL https://freenode.net/sasl/) in a short period, email kline@freenode.net when corrected. Thanks!","""reason used in dline"""))
conf.registerGlobalValue(Sigyn, 'torServer',
    registry.String("","""tor listing server"""))
conf.registerChannelValue(Sigyn, 'torPorts',
    registry.CommaSeparatedListOfStrings([''], """ports to check"""))
conf.registerChannelValue(Sigyn, 'torTarget',
    registry.String("","""ip of the targeted ircd, for tor checks"""))
# dronebl submit

conf.registerGlobalValue(Sigyn, 'droneblKey',
     registry.String("", """dronebl key for rpc calls""", private=True))
conf.registerGlobalValue(Sigyn, 'droneblHost',
     registry.String("http://dronebl.org/RPC2", """where bot must do rpc calls"""))

# report
conf.registerGlobalValue(Sigyn, 'reportChannel',
    registry.String("","""channel of the instance"""))
conf.registerGlobalValue(Sigyn, 'reportNick',
    registry.String("","""bot nicks starts with"""))
conf.registerGlobalValue(Sigyn, 'reportPermit',
    registry.Integer(-1,"""number of proxy detected, -1 to disable"""))
conf.registerGlobalValue(Sigyn, 'reportLife',
    registry.PositiveInteger(1,"""life duration of proxies, in seconds"""))
conf.registerGlobalValue(Sigyn, 'defcon',
    registry.PositiveInteger(1,"""duration of defcon mode in seconds, where bot is more agressive, with lowered abuse triggers and no ignores"""))

# amsg

conf.registerGlobalValue(Sigyn, 'amsgMinium',
    registry.PositiveInteger(1,"""length of text necessary to start amsg check"""))
conf.registerGlobalValue(Sigyn, 'amsgPermit',
    registry.Integer(-1,"""number of channels allowed with same message"""))
conf.registerGlobalValue(Sigyn, 'amsgLife',
    registry.PositiveInteger(1,"""life of channels in seconds"""))
conf.registerGlobalValue(Sigyn, 'amsgPercent',
    registry.Probability(1.00,"""percent of similarity between two messages"""))

# service notices 

# channel flood snote
conf.registerGlobalValue(Sigyn, 'channelFloodPermit',
    registry.Integer(-1,"""number of server notices (possible flooder) from various host allowed for a given channel"""))
conf.registerGlobalValue(Sigyn, 'channelFloodLife',
    registry.PositiveInteger(1,"""life of notices in seconds"""))

# user flood snote
conf.registerGlobalValue(Sigyn, 'userFloodPermit',
    registry.Integer(-1,"""number of snotes about flood targeted a given user with differents hosts"""))
conf.registerGlobalValue(Sigyn, 'userFloodLife',
    registry.PositiveInteger(1,"""life of notices in seconds"""))

# join/spam snote
conf.registerGlobalValue(Sigyn, 'joinRatePermit',
    registry.Integer(-1,"""number of snotes about join floodfor a given channel with differents users"""))
conf.registerGlobalValue(Sigyn, 'joinRateLife',
    registry.PositiveInteger(1,"""life of notices in seconds"""))

# NickServ ID failures

conf.registerGlobalValue(Sigyn, 'idPermit',
    registry.Integer(-1,"""number of snotes about id failure from a given user and different account"""))
conf.registerGlobalValue(Sigyn, 'idLife',
    registry.PositiveInteger(1,"""life duration of message in those snote"""))

# Quit flood
conf.registerChannelValue(Sigyn, 'brokenPermit',
    registry.Integer(-1,"""number of quit allowed"""))
conf.registerChannelValue(Sigyn, 'brokenLife',
    registry.PositiveInteger(1,"""life duration of buffer for broken client detection"""))
conf.registerChannelValue(Sigyn, 'brokenDuration',
    registry.PositiveInteger(1,"""kline duration in minutes"""))
conf.registerChannelValue(Sigyn, 'brokenReason',
    registry.String("Votre client IRC semble avoir un probleme et flood certains cannaux. Banni pour %s min. En cas d'erreur, contactez kline@ekinetirc.com.","""kline reason"""))
conf.registerChannelValue(Sigyn, 'brokenHost',
    registry.CommaSeparatedListOfStrings([''], """list of knowns broken host"""))


# if a mass join of efnet users happens, bot will enter in defcon mode
conf.registerChannelValue(Sigyn, 'efnetPermit',
    registry.Integer(-1,"""number of efnet joins allowed during efnetLife, -1 to disable"""))
conf.registerChannelValue(Sigyn, 'efnetLife',
    registry.PositiveInteger(1,"""life duration of join allowed from efnet users"""))
conf.registerChannelValue(Sigyn, 'efnetDuration',
    registry.PositiveInteger(1,"""active effect of efnet klines on join"""))
    
# can be per channel's settings
conf.registerChannelValue(Sigyn, 'ignoreChannel',
     registry.Boolean(False, """ignore everything in the channel"""))
conf.registerChannelValue(Sigyn, 'ignoreDuration',
     registry.Integer(-1, """in secondes: if -1 disabled, otherwise bot ignores user's privmsg/notices after <seconds> in channel"""))

# abuses lowered thresold for given channel and a given abuse, and lift ignores
conf.registerChannelValue(Sigyn, 'abusePermit',
    registry.Integer(1,"""-1 to disable, reduces threshold of triggers when they occurs more than abusePermit during abuseLife"""))
conf.registerChannelValue(Sigyn, 'abuseLife',
    registry.PositiveInteger(1,"""life duration of message in the buffer detection, in seconds"""))
conf.registerChannelValue(Sigyn, 'abuseDuration',
    registry.PositiveInteger(1,"""duration in seconds of abuse state"""))
    
# ignored users can still trigger klines if desired
conf.registerChannelValue(Sigyn, 'bypassIgnorePermit',
    registry.Integer(-1,"""number of triggers allowed while ignored, -1 to disable"""))
conf.registerChannelValue(Sigyn, 'bypassIgnoreLife',
    registry.PositiveInteger(1,"""in seconds"""))

# channel protections
conf.registerChannelValue(Sigyn, 'floodPermit',
    registry.Integer(-1,"""number of messages allowed during floodLife, -1 to disable"""))
conf.registerChannelValue(Sigyn, 'floodLife',
    registry.PositiveInteger(1,"""life duration of message in the flood buffer detection"""))
conf.registerChannelValue(Sigyn, 'floodMinimum',
    registry.PositiveInteger(1,"""minimun number of chars to enter flood detection"""))

conf.registerChannelValue(Sigyn, 'lowFloodPermit',
    registry.Integer(-1,"""number of messages allowed during lowFloodLife, -1 to disable"""))
conf.registerChannelValue(Sigyn, 'lowFloodLife',
    registry.PositiveInteger(1,"""life duration of message in the lowFlood buffer detection"""))

conf.registerChannelValue(Sigyn, 'repeatPermit',
    registry.Integer(1,"""number of repeated messages allowed during repeatLife"""))
conf.registerChannelValue(Sigyn, 'repeatLife',
    registry.PositiveInteger(1,"""life duration of message in the repeat buffer detection"""))
conf.registerChannelValue(Sigyn, 'repeatPercent',
    registry.Probability(1.00,"""percent of similarity between two messages to trigger repeat detection"""))
conf.registerChannelValue(Sigyn, 'repeatCount',
    registry.PositiveInteger(1,"""if pattern is smaller than computedPattern, bot may still add it anyway, if larger than repeatPattern"""))
conf.registerChannelValue(Sigyn, 'repeatPattern',
    registry.PositiveInteger(1,"""minimal length of a pattern, in that case, the pattern must be repeated more than at least repeatCount in the message"""))
    
conf.registerChannelValue(Sigyn, 'lowRepeatPermit',
    registry.Integer(-1,"""number of repeated messages allowed during repeatLife"""))
conf.registerChannelValue(Sigyn, 'lowRepeatLife',
    registry.PositiveInteger(1,"""life duration of message in the repeat buffer detection"""))
conf.registerChannelValue(Sigyn, 'lowRepeatPercent',
    registry.Probability(1.00,"""percent of similarity between two messages to trigger repeat detection"""))
conf.registerChannelValue(Sigyn, 'lowRepeatMinimum',
    registry.PositiveInteger(1,"""minimun number of chars to enter massRepeat detection"""))

conf.registerChannelValue(Sigyn, 'massRepeatPermit',
    registry.Integer(-1,"""number of mass repeat permit duration massRepeatLife, -1 to disable"""))
conf.registerChannelValue(Sigyn, 'massRepeatLife',
    registry.PositiveInteger(1,"""Duration of messages's life in massRepeat counter, in seconds"""))
conf.registerChannelValue(Sigyn, 'massRepeatPercent',
    registry.Probability(1.00,"""percentage similarity between previous and current message to trigger a massRepeat count"""))
conf.registerChannelValue(Sigyn, 'massRepeatMinimum',
    registry.PositiveInteger(1,"""minimun number of chars to enter massRepeat detection"""))

conf.registerChannelValue(Sigyn, 'computedPattern',
    registry.Integer(1,"""minimun number of chars needed to keep it as a spam pattern, -1 to disable"""))
conf.registerChannelValue(Sigyn, 'computedPatternLife',
    registry.Integer(1,"""minimun number of chars needed to keep it as a spam pattern, -1 to disable"""))

conf.registerChannelValue(Sigyn, 'lowMassRepeatPermit',
    registry.Integer(-1,"""number of mass repeat permit duration massRepeatLife, -1 to disable"""))
conf.registerChannelValue(Sigyn, 'lowMassRepeatLife',
    registry.PositiveInteger(1,"""Duration of messages's life in massRepeat counter, in seconds"""))
conf.registerChannelValue(Sigyn, 'lowMassRepeatPercent',
    registry.Probability(1.00,"""percentage similarity between previous and current message to trigger a massRepeat count"""))
conf.registerChannelValue(Sigyn, 'lowMassRepeatMinimum',
    registry.PositiveInteger(1,"""minimun number of chars to enter massRepeat detection"""))

conf.registerChannelValue(Sigyn, 'hilightNick',
    registry.Integer(-1,"""number nick allowed per message, -1 to disable"""))
conf.registerChannelValue(Sigyn, 'hilightPermit',
    registry.Integer(-1,"""number of hilight detection allowed during hilightLife, -1 to disable"""))
conf.registerChannelValue(Sigyn, 'hilightLife',
    registry.PositiveInteger(1,"""life duration of hilight buffer"""))
    
conf.registerChannelValue(Sigyn, 'lowHilightNick',
    registry.Integer(-1,"""number nick allowed per message, -1 to disable"""))
conf.registerChannelValue(Sigyn, 'lowHilightPermit',
    registry.Integer(-1,"""number of hilight detection allowed during hilightLife, -1 to disable"""))
conf.registerChannelValue(Sigyn, 'lowHilightLife',
    registry.PositiveInteger(1,"""life duration of hilight buffer"""))

conf.registerChannelValue(Sigyn, 'cyclePermit',
    registry.Integer(-1,"""number of cycle allowed during cycleLife"""))
conf.registerChannelValue(Sigyn, 'cycleLife',
    registry.PositiveInteger(1,"""life duration of part/quit in the cycle buffer detection"""))

conf.registerChannelValue(Sigyn, 'ctcpPermit',
    registry.Integer(-1,"""number of channel's ctcp allowed"""))
conf.registerChannelValue(Sigyn, 'ctcpLife',
    registry.PositiveInteger(1,"""life duration ofchannel's ctcp buffer detection"""))

conf.registerChannelValue(Sigyn, 'nickPermit',
    registry.Integer(-1,"""number of nick change allowed during cycleLife"""))
conf.registerChannelValue(Sigyn, 'nickLife',
    registry.PositiveInteger(1,"""life duration of nick changes buffer detection"""))
