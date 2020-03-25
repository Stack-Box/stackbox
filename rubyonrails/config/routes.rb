Rails.application.routes.draw do
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
  get 'mysql_view_stacks' => "stacks#view_stacks", :as => :view_stacks
  get 'stacks/view_stacks'
end
