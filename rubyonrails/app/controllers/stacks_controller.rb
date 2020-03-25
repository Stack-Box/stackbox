class StacksController < ApplicationController
  def view_stacks
    @stacks = Stack.all
    render json: @stacks
  end
end
