ACMS.Dispatch.Admin.Configunit=function(context){var Configunit=arguments.callee;var $input=$(':input[name^="ACMS_POST_Config"]',context);if($input.size()){var form=$input.get(0).form;$(".column-definition-wrapper",form).each(function(){var wrapper=this;$(wrapper).sortable({handle:".handle",axis:"y",zIndex:999,opacity:0.6,out:function(){$(".handle",wrapper).removeClass(ACMS.Config.hoverClass)}});$('[class^="column_def_"]',wrapper).each(function(){$(this).click(function(){Configunit._add(this.className,
wrapper);return false})});$(".trigger-delete",wrapper).each(function(){Configunit.remove(this)})})}};ACMS.Dispatch.Admin.Configunit._add=function(column,target){var Config=ACMS.Config;var Configunit=this;var url=ACMS.Library.acmsLink({tpl:"ajax/unit.html"},true);var data={column:column,rid:Config.rid};$.get(url,data,function(html){var $html=$(html);$(".trigger-delete",$html).each(function(){Configunit.remove(this)});$(target).append($html)})};
ACMS.Dispatch.Admin.Configunit.remove=function(elm){$(elm).click(function(){console.log();$(this).parents('[class^="column-definition-"]').eq(0).remove();return false})};
