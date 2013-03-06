$(function() {
	$("#id_start_date").datepicker({ dateFormat: 'yy-mm-dd' });
	$("#id_end_date").datepicker({ dateFormat: 'yy-mm-dd' });

	$("#delete_link").on("click", function(){
		if(!confirm("Are you sure you want to continue your delete session?"))
		{
			return false;
		}
	})
});