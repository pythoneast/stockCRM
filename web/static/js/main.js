$(document).on("click", ".openSellProductForm", function () {
  var productId = $(this).data('id');
  $("#id_product_id").val(productId);
});

$(document).on("click", ".openDeleteProductForm", function () {
  var productId = $(this).data('id');
  var productTitle = $(this).data('title');
  console.log(productId, productTitle);
  $("#id_prod_id").val(productId);
  $("#productTitle").html(productTitle);
});