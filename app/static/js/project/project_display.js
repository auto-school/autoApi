
$(document).ready(function(){

    types_map = ['国创', '上创', 'SITP', '挑战杯', '创新赛事', '企业课题', '创业项目', '其他']

    $('.pro_type').each(function(){
        $(this).text(types_map[parseInt($(this).text())])
    })

    $('button.attend-project').click(function(){
        $('div.attend-project').modal({show:true})
        var applied_project_id = $(this).prev().text()
        $('input#applied-project').val(applied_project_id)
    });
})

