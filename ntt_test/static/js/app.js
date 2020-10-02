function createRouter() {
    let token = $('input[name=csrfmiddlewaretoken]').val();
    let name = $('input[name=name]').val();
    let ip_add = $('input[name=ip_address]').val();
    let id = $('input[name="update_id"]').val();
    if (id) {
        $.ajax({
            headers: { "X-CSRFToken": token },
            type: 'post',
            url: '/create-router/',
            data: {
                'token': token,
                'name': name,
                'ip_add': ip_add,
                'id': id
            },
            dataType: 'json',
            success: function(data) {
                $('#router_details').replaceWith(
                    "<tr>" +
                    "<td>" +data.id  +"</td>" +
                    "<td>" +data.name  +"</td>" +
                    "<td>" + data.ip_add  +"</td>" +
                    "<td colspan="+"2" + ">" + 
                        "<span onclick=" + `editRouter(data.id)` +"> Edit </span> |" +
                        "<span onclick=" + `deleteRouter(data.id)` +">Delete</span>" +"</td>"
                    +"</tr>"
                )

            },
            error: function(err) {
                console.log(err)
            }
        });
    }

    if (name) {
        $.ajax({
            headers: { "X-CSRFToken": token },
            type: 'post',
            url: '/create-router/',
            data: {
                'token': token,
                'name': name,
                'ip_add': ip_add,
                'id': id
            },
            dataType: 'json',
            success: function(data) {
                $('#router_details').append(
                    "<tr>" +
                    "<td>" +data.id  +"</td>" +
                    "<td>" +data.name  +"</td>" +
                    "<td>" + data.ip_add  +"</td>" +
                    "<td colspan="+"2" + ">" + 
                        "<span onclick=" + `editRouter(data.id)` +"> Edit </span> |" +
                        "<span onclick=" + `deleteRouter(data.id)` +">Delete</span>" +"</td>"
                    +"</tr>"
                )
                let counter_id = $('.counter_id').last().html();
                if (counter_id) {
                    window.top.location = window.top.location;
                }
                else if(counter_id == null) {
                    location.reload();
                }

            },
            error: function(err) {
                console.log(err)
            }
        })
    }
    if (!name) {
        alert('Name is required');
    }
    
}



function tableDetails() {
    let tableData = []
    let x = document.getElementsByClassName('counter_id')
    for (let i=0; i < x.length; i++) {
        tableData.push(x[i].innerHTML);
    }
    
    return tableData;
}




function editRouter(id) {
    
    if (id) {
        $.ajax({
            url: '/router/' +id,
            data: {
                'id': id
            },
            dataType: 'json',
            success: function(data) {
                $('input[name="update_id"]').val(data.id);
                $('input[name="name"]').val(data.name);
                $('input[name="ip_address"]').val(data.ip_add);
            },
            error: function(err) {
                console.log(err)
            }            
        })
        
        
    }

}

function deleteRouter(id) {
    let token = $('input[name=csrfmiddlewaretoken]').val();
    console.log(token);
    if (id) {
        $.ajax({
            headers: { "X-CSRFToken": token },
            type: 'post',
            url: '/deleteRouter/',
            data: {
                'id': id
            },
            dataType: 'json',
            success: function(data) {
                location.reload();
            },
            error: function(err) {
                console.log(err)
            }
        })
    }

    console.log(id);
}

function generateRecords() {
    let v = prompt("How number of you want create? ");
    console.log(v);
    if (v) {
        $.ajax({
            url: '/generateRecords/',
            data: {
                'id': v
            },
            dataType: 'json',
            success: function(data) {
                $('#router_details').append(
                    "<tr>" +
                    "<td>" + data.id  +"</td>" +
                    "<td>" + data.name  +"</td>" +
                    "<td>" + data.ip_add  +"</td>" +
                    "<td colspan="+"2" + ">" + 
                        "<span onclick=" + `editRouter(data.id)` +"> Edit </span> |" +
                        "<span onclick=" + `deleteRouter(data.id)` +">Delete</span>" +"</td>"
                    +"</tr>"
                )
            },
            error: function(err) {
                console.log(err)
            }
        })

        window.top.location = window.top.location;
    }
    
}